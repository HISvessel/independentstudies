"""this is a second example for our tutorial into opencv

this one is an edge detector module that finds the edges inside of a photo
and shows the results"""

import cv2

# Load image from files
img = cv2.imread("pic-work-03.jpg")


#Rotating an image
#we can rotate the image by giving the cve argument with the builtin dimension as the parameter
#cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)
#Resizing an image
#we resize the image by dimension in height and width(remember HTML) and basedon coordinates


# Show results
cv2.imshow("Original", img) #image show(imshow) takes two parameters
cv2.imshow("Edges", edges)#the image, and the name of the window in which the image is opened
cv2.waitKey(0)#wait for until an input is given, can be given a value above 1 to wait in seconds
cv2.destroyAllWindows()#terminates the process