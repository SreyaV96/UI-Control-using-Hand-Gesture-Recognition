# UI-Control-using-Hand-Gesture-Recognition
This project enables hand gesture-based navigation of a web-based visual system using MediaPipe, Flask, and JavaScript. Users can swipe left/right to navigate pages and pause with an open palm, creating a seamless, touch-free experience

1. Introduction
The Hand Gesture Controlled Visual Information System is a web-based application that allows users to control an image slideshow using hand gestures. The system leverages MediaPipe for hand gesture recognition, OpenCV for video processing, and Flask to serve the web interface.
2. Features
•	Hand Gesture Recognition using MediaPipe
•	Flask Backend to serve the web page
•	JavaScript & WebSockets for real-time control
•	Automatic Slideshow that changes every 5 seconds
•	Hand Gesture Controls: 
o	Open Palm → Pause Slideshow
o	Left Pointed Index Finger → Move to Previous Slide
o	Right Pointed Index Finger → Move to Next Slide
3. Technologies Used
•	Python (Flask, OpenCV, MediaPipe)
•	HTML, CSS, JavaScript (Frontend UI)
•	WebSockets / Fetch API (Real-time communication)
4. System Architecture
The system consists of:
1.	Frontend (index.html): Displays the slideshow and webcam feed.
2.	Backend (app.py): Handles hand tracking and serves the web application.
3.	Gesture Recognition Module: Detects hand gestures using MediaPipe.
5. Installation & Setup
5.1 Install Required Packages
Ensure Python is installed, then install dependencies using:
pip install flask opencv-python mediapipe
5.2 Run the Flask Application
python app.py
This starts the web server, accessible at http://127.0.0.1:5000/.
6. Code Explanation
6.1 index.html (Frontend UI)
•	Displays the slideshow and webcam feed.
•	Uses JavaScript to fetch the latest slide index from the backend.
6.2 app.py (Backend & Gesture Detection)
•	Flask Web Server: Serves the web page and manages communication.
•	OpenCV & MediaPipe: Captures webcam input and detects gestures.
•	Gesture Handling: Updates slideshow based on detected gestures.
•	Slideshow Control: Automatically switches slides every 5 seconds unless paused.
7. Working Mechanism
1.	The user opens the web page.
2.	The webcam feed starts, and hand gestures are detected.
3.	Based on gestures: 
o	Open palm pauses the slideshow.
o	Left-pointed finger moves to the previous slide.
o	Right-pointed finger moves to the next slide.
4.	The slideshow automatically switches every 5 seconds if not paused.
8. Future Improvements
•	Support for additional gestures.
•	Improved gesture detection accuracy.
•	Enhancing UI/UX for better interaction.
9. Conclusion
This project demonstrates a real-time hand gesture-controlled web application, making interaction more intuitive and touch-free. By leveraging computer vision and Flask, it provides a dynamic and engaging user experience.
