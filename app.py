from flask import Flask, render_template, Response, jsonify
import os
import cv2
import mediapipe as mp
import time
import threading

app = Flask(__name__)

# Initialize MediaPipe Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.70, min_tracking_confidence=0.70)
mp_draw = mp.solutions.drawing_utils

# Load Images for Slideshow
image_folder = os.path.join('static', 'images')
image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg', 'gif', 'jfif'))]
current_index = 0
paused = False
index_lock = threading.Lock()
last_gesture_time = time.time()  # Track last gesture time
last_gesture = None  # Track the last gesture

cap = cv2.VideoCapture(0)
webcam_active = True

def detect_gesture(frame):
    """Detects gestures for one hand only (pause, swipe left, swipe right)."""
    global current_index, paused, last_gesture_time, last_gesture
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if not result.multi_hand_landmarks:
        paused = False  # Resume slideshow when no hand is detected
        return

    # Process only the first detected hand
    hand_landmarks = result.multi_hand_landmarks[0]
    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Extract landmark positions
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

    # Detect Open Palm (Pause Slideshow)
    extended_fingers = sum(
        hand_landmarks.landmark[t].y < hand_landmarks.landmark[p].y
        for t, p in zip(
            [mp_hands.HandLandmark.THUMB_TIP,
             mp_hands.HandLandmark.INDEX_FINGER_TIP,
             mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
             mp_hands.HandLandmark.RING_FINGER_TIP,
             mp_hands.HandLandmark.PINKY_TIP],
            [mp_hands.HandLandmark.THUMB_IP,
             mp_hands.HandLandmark.INDEX_FINGER_PIP,
             mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
             mp_hands.HandLandmark.RING_FINGER_PIP,
             mp_hands.HandLandmark.PINKY_PIP]
        )
    )

    current_time = time.time()

    if extended_fingers >= 4:  # Open Palm Detected
        if last_gesture != "pause" or (current_time - last_gesture_time > 5):
            paused = True
            last_gesture = "pause"
            last_gesture_time = current_time
            print("⏸ Open Palm Detected - Pausing Slideshow")
        return

    # Check if the index finger is pointing left or right
    if index_tip.x < index_mcp.x:  # Left-pointed index finger (Move to previous slide)
        if last_gesture != "left" or (current_time - last_gesture_time > 5):
            with index_lock:
                current_index = (current_index - 1) % len(image_files)
            last_gesture = "left"
            last_gesture_time = current_time
            print("⬅️ Left-Pointed Index Finger Detected - Previous Slide")
            paused = False  # Resume slideshow
    elif index_tip.x > index_mcp.x:  # Right-pointed index finger (Move to next slide)
        if last_gesture != "right" or (current_time - last_gesture_time > 5):
            with index_lock:
                current_index = (current_index + 1) % len(image_files)
            last_gesture = "right"
            last_gesture_time = current_time
            print("➡️ Right-Pointed Index Finger Detected - Next Slide")
            paused = False  # Resume slideshow

def generate_frames():
    """Captures webcam frames and processes gestures."""
    global webcam_active
    cap = cv2.VideoCapture(0)
    while webcam_active:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)  # Fix mirroring issue (Flip horizontally)
        detect_gesture(frame)

        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    cap.release()

def slideshow():
    """Auto-slideshow thread that waits 5 seconds before changing slides."""
    global current_index, paused, last_gesture_time
    while True:
        if not paused and (time.time() - last_gesture_time > 5):  # Wait 5 seconds before switching
            with index_lock:
                current_index = (current_index + 1) % len(image_files)
            last_gesture_time = time.time()
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html', images=image_files, current_index=current_index)

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_current_index')
def get_current_index():
    return jsonify({'current_index': current_index})

if __name__ == '__main__':
    threading.Thread(target=slideshow, daemon=True).start()
    app.run(debug=True)