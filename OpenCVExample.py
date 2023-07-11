
import numpy as np
import cv2

def canny_edge_detection(image, threshold1, threshold2):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, threshold1, threshold2)

    return edges

# Load input image
#image = cv2.imread("C:/Users/david/github/CannyEdgeDetection/funnyCat.webp")
image = cv2.imread('C:/Users/david/OneDrive/Pictures/funnyCat.webp')


# Define threshold values (adjust as needed)
threshold1 = 20
threshold2 = 60

# Apply Canny edge detection
edges = canny_edge_detection(image, threshold1, threshold2)

# Display the original image and the edges
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
