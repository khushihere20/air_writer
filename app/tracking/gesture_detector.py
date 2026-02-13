class GestureDetector:

    def __init__(self):
        pass

    def fingers_up(self, landmarks):
        """
        Returns number of fingers up
        """
        if not landmarks:
            return 0

        fingers = []

        # Landmark indices
        tips = [8, 12]        # Index, Middle
        pips = [6, 10]        # Their PIP joints

        for tip, pip in zip(tips, pips):
            if landmarks[tip][2] < landmarks[pip][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return sum(fingers)

    def get_mode(self, landmarks):
        count = self.fingers_up(landmarks)

        if count == 1:
            return "WRITE"
        elif count == 2:
            return "ERASE"
        else:
            return "IDLE"