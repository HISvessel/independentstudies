import math
import numpy as np

class FormAnalyzer:
    @staticmethod
    def angle_between(p1, p2, p3):
        """A static method to find the angle between the given arguments.
        Arguments:
        p1: the first joint to interpret
        p2: the second joint to interpret
        p3:the third joint to interpret"""

        v1 = (p1.x - p2.x, p1.y - p2.y)
        v2 = (p3.x - p2.x, p3.y - p2.y)

        dot = v1[0]*v2[0] + v1[1]*v2[1]

        mag1 = math.hypot(*v1); mag2 = math.hypot(*v2)

        if mag1 == 0 or mag2 == 0:
            return None
        return math.degrees(math.acos(dot / (mag1*mag2)))

    @staticmethod
    def calculate_angle(p1, p2, p3):
        """A sample test to compare agains the previous angle between function"""
        ba = np.array(p1) - np.array(p2)
        bc = np.array(p3) - np.array(p2)

        cosang = np.dot(ba,bc) / np.linalg.norm(ba) * np.linalg.norm(bc)

        ang = np.degrees(np.arccos(np.clip(cosang, -1.0, 1.0)))
        return ang