import cv2
from app.config import *
from app.tracking.hand_tracker import HandTracker
from app.tracking.gesture_detector import GestureDetector
from app.engine.drawing_engine import DrawingEngine
from app.ui.toolbar import Toolbar


class AirWriterApp:

    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.hand_tracker = HandTracker()
        self.gesture_detector = GestureDetector()
        self.drawing_engine = DrawingEngine()
        self.toolbar = Toolbar()

        self.current_mode = "WRITE"   # Persistent mode
        self.running = True

    def run(self):
        while self.running:
            success, frame = self.cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)

            # ---------------- HAND TRACKING ----------------
            results = self.hand_tracker.process_frame(frame)
            frame = self.hand_tracker.draw_landmarks(frame, results)
            landmarks = self.hand_tracker.get_landmarks(frame, results)

            # Default mode from gesture
            gesture_mode = self.gesture_detector.get_mode(landmarks)

            # ---------------- FINGER POSITION ----------------
            if landmarks and len(landmarks) > 8:
                x = landmarks[8][1]   # x coordinate
                y = landmarks[8][2]   # y coordinate

                # ---------------- TOOLBAR CLICK CHECK ----------------
                clicked = self.toolbar.check_click(x, y)

                if clicked == "CLEAR":
                    self.drawing_engine.canvas = None

                elif clicked == "SAVE":
                    if self.drawing_engine.canvas is not None:
                        cv2.imwrite("air_drawing.png", self.drawing_engine.canvas)

                elif clicked == "COLOR":
                    # Update brush color
                    self.drawing_engine.set_color(self.toolbar.active_color)

                elif clicked in ["DRAW", "ERASE"]:
                    self.current_mode = clicked

                else:
                    # If nothing clicked → use gesture mode
                    self.current_mode = gesture_mode

                # ---------------- DRAWING ----------------
                frame = self.drawing_engine.draw(
                    frame,
                    x,
                    y,
                    self.current_mode
                )

            else:
                # Reset smooth continuity if no hand
                self.drawing_engine.prev_x = None
                self.drawing_engine.prev_y = None

            # ---------------- UI DRAW ----------------
            frame = self.toolbar.draw(frame)

            # Mode display
            cv2.putText(
                frame,
                f"Mode: {self.current_mode}",
                (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            cv2.imshow(WINDOW_NAME, frame)

            # ESC to exit
            if cv2.waitKey(1) & 0xFF == 27:
                self.running = False

        self.cleanup()

    def cleanup(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = AirWriterApp()
    app.run()