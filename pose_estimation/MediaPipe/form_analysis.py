import math
import numpy as np
from collections import deque

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
        return math.degrees(math.asin(dot / (mag1*mag2)))

    @staticmethod
    def calculate_angle(p1, p2, p3):
        """A sample test to compare agains the previous angle between function"""
        #importing our data to process into numpy arrays
        a = np.array(p1)
        b = np.array(p2)
        c = np.array(p3)

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0/np.pi)

        if angle > 180.0:
            angle = 360 - angle
        return angle
    
    @staticmethod
    def calculate_flare_angle(p1, p2, p3):
        a = np.array(p1)
        b = np.array(p2)
        c = np.array(p3)
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0/np.pi)

        if angle > 180.0:
            angle = 360 - angle
        return angle

    @staticmethod
    def calculate_body_angle(p1, p2, p3):
        """A sample test to compare agains the previous angle between function"""
        #importing our data to process into numpy arrays
        a = np.array(p1)
        b = np.array(p2)
        c = np.array(p3)

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b [0])
        angle = np.abs(radians * 180.0/np.pi)

        return angle
    
    def normalize_landmarks(landmarks):
        left_hip = landmarks[23]
        right_hip = landmarks[24]
