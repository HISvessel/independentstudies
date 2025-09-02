"""in this tutorial we will learn to smoothen images by use of
various OpenCV functions that explore linear filters, such as

blur()
GaussianBlur()
medianBlur()
bilateralFilter()

Linear filters: 

Smoothing, or blurring, is a simple image processing operation. Smoothing images
is possible by applying filters to images. The most common of these filter types are
linear, in which pixel values at output are determined as a weighted sum of input pixel
values.

The filter cuocient is determined by the following operation: g(i,j) = \sum_{k,l} f(i+k, j+l) h(k,l)

h(k, l) is called the kernel, aka, the coefficients of the filter
It helps to visualize a filter as a window of coefficients sliding across an image.


Types of filters:
Normalized box Filter

Gaussian Filter"""


import sys
import cv2 as cv
import numpy as np
 
#  Global Variables
 
DELAY_CAPTION = 1500 #what is this number? this will delay caption by 1.5 second, perhaps?
DELAY_BLUR = 100 #what is this number? this will delay the blur by .1 second, perhaps?
MAX_KERNEL_LENGTH = 31 #what is this number?
 
src = None #indicates file source, None if it does not exist
dst = None #recieves the source file for filtering, None if src is None
window_name = 'Smoothing Demo'
 
 
def main(argv):
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
 
    # Load the source image
    imageName = argv[0] if len(argv) > 0 else 'lena.jpg'
 
    global src
    src = cv.imread(cv.samples.findFile(imageName))
    if src is None:
        print ('Error opening image')
        print ('Usage: smoothing.py [image_name -- default ../data/lena.jpg] \n')
        return -1
 
    if display_caption('Original Image') != 0:
        return 0
 
    global dst
    dst = np.copy(src)
    if display_dst(DELAY_CAPTION) != 0:
        return 0
 
    # Applying Homogeneous blur
    if display_caption('Homogeneous Blur') != 0:
        return 0
 
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv.blur(src, (i, i))
        if display_dst(DELAY_BLUR) != 0:
            return 0
    
 
    # Applying Gaussian blur
    if display_caption('Gaussian Blur') != 0:
        return 0
 
    
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv.GaussianBlur(src, (i, i), 0)
        if display_dst(DELAY_BLUR) != 0:
            return 0
    
 
    # Applying Median blur
    if display_caption('Median Blur') != 0:
        return 0
 
    
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv.medianBlur(src, i)
        if display_dst(DELAY_BLUR) != 0:
            return 0
    
 
    # Applying Bilateral Filter
    if display_caption('Bilateral Blur') != 0:
        return 0
 
    
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv.bilateralFilter(src, i, i * 2, i / 2)
        if display_dst(DELAY_BLUR) != 0:
            return 0
    
 
    #  Done
    display_caption('Done!')
 
    return 0
 
 
def display_caption(caption):
    global dst
    dst = np.zeros(src.shape, src.dtype)
    rows, cols, _ch = src.shape
    cv.putText(dst, caption,
                (int(cols / 4), int(rows / 2)),
                cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
 
    return display_dst(DELAY_CAPTION)
 
 
def display_dst(delay):
    cv.imshow(window_name, dst)
    c = cv.waitKey(delay)
    if c >= 0 : return -1
    return 0
 
 
if __name__ == "__main__":
    main(sys.argv[1:])