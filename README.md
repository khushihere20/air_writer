**🖊️ AirWriter – Real-Time Gesture Controlled Drawing System**

AirWriter is a real-time computer vision application that enables touchless writing and drawing using hand gestures. Built using Python, OpenCV, and MediaPipe, the system detects and tracks 21 hand landmarks to translate finger movements into smooth digital strokes with high responsiveness.
This project demonstrates practical implementation of real-time gesture recognition, state-based interaction design, and UI overlay systems.

**🚀 Key Highlights**
1. Real-time hand landmark detection (21-point tracking)
2. Gesture-based mode switching (Draw / Erase)
3. Smooth stroke interpolation for natural writing
4. Interactive UI toolbar with circular color swatches
5. Canvas state management (Clear / Save functionality)
6. Modular architecture (tracking, engine, UI separation)
7. Optimized for performance and low latency

**🧠 Technical Concepts Demonstrated**
1. Computer Vision (CV)
2. Real-time video frame processing
3. Gesture recognition logic
4. Human-computer interaction (HCI)
5. State management in interactive systems
6. Modular software architecture
7. Event-driven UI overlay design

**🛠 Tech Stack**
- Python 3.10+
- OpenCV
- MediaPipe
- NumPy

**📂 Architecture Overview**
app/
 ├── tracking/        # Hand tracking & gesture detection
 ├── engine/          # Drawing logic & stroke smoothing
 ├── ui/              # Toolbar & interface rendering
 └── main.py          # Application controller
The system follows a clean modular structure separating tracking, gesture logic, rendering engine, and UI components.

**▶️ How to Run**
pip install -r requirements.txt
python run.py
Press ESC to exit.

**💡 Future Scope**
- Undo/Redo functionality
- Brush thickness & dynamic stroke control
- Gesture-based UI navigation
- Multi-hand support
- AI-based handwriting recognition

**👩‍💻 Developed By**
Noopur Awasthi

