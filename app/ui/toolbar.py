import cv2
import numpy as np


class Toolbar:

    def __init__(self):
        self.height = 100

        self.colors = {
            "BLUE": ((255, 0, 0), 550),
            "RED": ((0, 0, 255), 600),
            "GREEN": ((0, 255, 0), 650),
            "YELLOW": ((0, 255, 255), 700),
            "WHITE": ((255, 255, 255), 750),
        }

        self.active_color = (255, 0, 0)

        self.buttons = {
            "DRAW": (20, 20, 120, 70),
            "ERASE": (140, 20, 240, 70),
            "CLEAR": (260, 20, 360, 70),
            "SAVE": (380, 20, 480, 70),
        }

    def draw(self, frame):
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (frame.shape[1], self.height), (25, 25, 25), -1)
        frame = cv2.addWeighted(overlay, 0.85, frame, 0.15, 0)

        # Draw rectangular buttons
        for name, (x1, y1, x2, y2) in self.buttons.items():
            cv2.rectangle(frame, (x1, y1), (x2, y2), (60, 60, 60), -1)
            cv2.putText(frame, name, (x1 + 15, y1 + 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Draw circular color swatches
        for name, (color, x_pos) in self.colors.items():
            thickness = 4 if color == self.active_color else -1
            cv2.circle(frame, (x_pos, 50), 25, color, thickness)

        return frame

    def check_click(self, x, y):
        # Check rectangular buttons
        for name, (x1, y1, x2, y2) in self.buttons.items():
            if x1 < x < x2 and y1 < y < y2:
                return name

        # Check circular color buttons
        for name, (color, x_pos) in self.colors.items():
            distance = ((x - x_pos) ** 2 + (y - 50) ** 2) ** 0.5
            if distance < 25:
                self.active_color = color
                return "COLOR"

        return None