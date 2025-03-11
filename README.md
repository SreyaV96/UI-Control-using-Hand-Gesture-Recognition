# UI-Control-using-Hand-Gesture-Recognition
## 1. Introduction
The Hand Gesture Controlled Visual Information System is a web-based application that allows users to control an image slideshow using hand gestures. The system leverages MediaPipe for hand gesture recognition, OpenCV for video processing, and Flask to serve the web interface.
## 2. Features
   - Hand Gesture Recognition using MediaPipe
   - Flask Backend to serve the web page
<<<<<<< HEAD
   - JavaScript & AJAX for real-time control
   - Automatic Slideshow that changes every 3 seconds
=======
   - JavaScript & WebSockets for real-time control
   - Automatic Slideshow that changes every 5 seconds
>>>>>>> e2e1605c5238c6e7d57206cd0553c9887e401306
   - Hand Gesture Controls: 
     - Open Palm → Pause Slideshow
     - Left Pointed Index Finger → Move to Previous Slide
     - Right Pointed Index Finger → Move to Next Slide
## 3. Technologies Used
  -	Python (Flask, OpenCV, MediaPipe)
  -	HTML, CSS, JavaScript (Frontend UI)
<<<<<<< HEAD
  -	AJAX (Real-time communication)
=======
  -	WebSockets / Fetch API (Real-time communication)
>>>>>>> e2e1605c5238c6e7d57206cd0553c9887e401306
## 4. System Architecture
The system consists of:
1.	Frontend (index.html): Displays the slideshow and webcam feed.
2.	Backend (app.py): Handles hand tracking and serves the web application.
3.	Gesture Recognition Module: Detects hand gestures using MediaPipe.
## 5. Installation & Setup
### 5.1 Install Required Packages
Ensure Python is installed, then install dependencies using:

pip install flask opencv-python mediapipe
<<<<<<< HEAD

### 5.2 Run the Flask Application

python app.py

This starts the web server, which can be accessed locally.
## 6. Code Explanation
### 6.1 index.html (Frontend UI)
 -	Displays the slideshow and webcam feed.
 -	Uses JavaScript to fetch the latest slide index from the backend.
### 6.2 app.py (Backend & Gesture Detection)
 -  Flask Web Server: Serves the web page and manages communication.
 - 	OpenCV & MediaPipe: Captures webcam input and detects gestures.
 -	Gesture Handling: Updates slideshow based on detected gestures.
 -	Slideshow Control: Automatically switches slides every 3 seconds unless paused.
=======
### 5.2 Run the Flask Application
python app.py
This starts the web server, accessible at http://127.0.0.1:5000/.
## 6. Code Explanation
### 6.1 index.html (Frontend UI)
•	Displays the slideshow and webcam feed.
•	Uses JavaScript to fetch the latest slide index from the backend.
### 6.2 app.py (Backend & Gesture Detection)
•	Flask Web Server: Serves the web page and manages communication.
•	OpenCV & MediaPipe: Captures webcam input and detects gestures.
•	Gesture Handling: Updates slideshow based on detected gestures.
•	Slideshow Control: Automatically switches slides every 5 seconds unless paused.
>>>>>>> e2e1605c5238c6e7d57206cd0553c9887e401306
## 7. Working Mechanism
1.	The user opens the web page.
2.	The webcam feed starts, and hand gestures are detected.
3.	Based on gestures: 
    - Open palm pauses the slideshow.
    -	Left-pointed finger moves to the previous slide.
    - Right-pointed finger moves to the next slide.
<<<<<<< HEAD
4.	The slideshow automatically switches every 3 seconds if not paused.
=======
4.	The slideshow automatically switches every 5 seconds if not paused.
>>>>>>> e2e1605c5238c6e7d57206cd0553c9887e401306
## 8. Future Improvements
- Support for additional gestures.
-	Improved gesture detection accuracy.
- Enhancing UI/UX for better interaction.
## 9. Conclusion
<<<<<<< HEAD
This project demonstrates a real-time hand gesture-controlled web application, making interaction more intuitive and touch-free. By leveraging computer vision and Flask, it provides a dynamic and engaging user experience.
=======
This project demonstrates a real-time hand gesture-controlled web application, making interaction more intuitive and touch-free. By leveraging computer vision and Flask, it provides a dynamic and engaging user experience.
>>>>>>> e2e1605c5238c6e7d57206cd0553c9887e401306
