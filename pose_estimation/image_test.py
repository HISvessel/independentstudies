"""this is a second example for our tutorial into opencv

this one is an edge detector module that finds the edges inside of a photo
and shows the results"""

import cv2

# Load image
img = cv2.imread("pic-work-03.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()