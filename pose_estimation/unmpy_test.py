#!/usr/bin/env python3
"""this is our introduction to numpy, a Python math framework
for manipulation of data contained in arrays"""

import numpy as np

#these are array reading contained as an x, y axis of a cartesian plane
a = np.array([0, 0]) #center of a unitary circle
b = np.array([0, 1]) #90 degrees in a unit circle, or y = 1
c = np.array([1, 1]) #0 degrees in a unit circle, starting position

ba = a - b
bc = c - b


cos_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle = np.degrees(np.arccos(cos_angle))
print(f"Angle at B: {angle:.2f} degrees")
