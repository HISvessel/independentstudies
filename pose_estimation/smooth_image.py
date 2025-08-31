"""in this tutorial we will learn to smoothen images by use of
various OpenCV functions that explore linear filters, such as

blur()
GaussianBlur()
medianBlur()
bilateralFilter()

Linear filters: 

Smoothing, or blurring,  is a simple image processing operation"""


import cv2 as cv
import numpy as np
import sys


DELAY_CAPTURE = 1500
DELAY_BLUR = 100
MAX_KERNEL_LENGTH = 31

src = None
dest = None
window_name = "smoothing demo"

def main(argv):
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    imageName = argv[0] if len(argv) > 0 else "lena.jpg"