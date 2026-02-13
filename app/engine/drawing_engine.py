import cv2
import numpy as np
from app.config import *


class DrawingEngine:

    def __init__(self):
        self.canvas = None
        self.prev_x = None
        self.prev_y = None

        self.alpha = 0.2
        self.min_distance = 4

        self.color = (255, 0, 0)   # Default blue
        self.thickness = DRAW_THICKNESS

    def initialize_canvas(self, frame):
        if self.canvas is None:
            self.canvas = np.zeros_like(frame)

    def smooth_point(self, x, y):
        if self.prev_x is None:
            return x, y

        smooth_x = int(self.alpha * x + (1 - self.alpha) * self.prev_x)
        smooth_y = int(self.alpha * y + (1 - self.alpha) * self.prev_y)
        return smooth_x, smooth_y

    def set_color(self, color):
        self.color = color

    def draw(self, frame, x, y, mode):
        self.initialize_canvas(frame)

        if mode == "WRITE":
            x, y = self.smooth_point(x, y)

            if self.prev_x is not None:
                distance = ((x - self.prev_x) ** 2 + (y - self.prev_y) ** 2) ** 0.5

                if distance > self.min_distance:
                    cv2.line(
                        self.canvas,
                        (self.prev_x, self.prev_y),
                        (x, y),
                        self.color,
                        self.thickness,
                        cv2.LINE_AA
                    )

            self.prev_x, self.prev_y = x, y

        elif mode == "ERASE":
            cv2.circle(self.canvas, (x, y), 35, (0, 0, 0), -1)
            self.prev_x, self.prev_y = None, None

        else:
            self.prev_x, self.prev_y = None, None

        return cv2.add(frame, self.canvas)