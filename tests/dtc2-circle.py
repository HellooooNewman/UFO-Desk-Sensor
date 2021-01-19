# Works but isn't accurate at a distance
# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2

FOCAL_LENGTH = 906.107
RADIUS_OF_MARKER = 1.5
vid = cv2.VideoCapture(0)

low_red = np.array([0, 50, 50])
high_red = np.array([179, 255, 255])


def isPixelRed(image, x, y):
    if x < 0 or y < 0:
        return False

    img_height, img_width, _ = image.shape

    for i in range(img_height):
        for j in range(img_width):
            if (image[i][j][1] >= low_red).all() and (image[i][j][1] <= high_red).all():
                return True


def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    detected_circles = cv2.HoughCircles(gray_blurred,
                                        cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                        param2=30, minRadius=30, maxRadius=40)

    # compute the bounding box of the of the paper region and return it
    return detected_circles


def distance_to_camera(rad):
    # compute and return the distance from the maker to the camera
    return str((FOCAL_LENGTH * RADIUS_OF_MARKER) / rad)


while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # load the image, find the marker in the image, then compute the
    # distance to the marker from the camera
    detected_circles = find_marker(frame)

    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            dText = "Distance: " + distance_to_camera(r)
            cv2.putText(frame, dText,
                        (frame.shape[1] - 400, frame.shape[0] -
                         20), cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0), 3)

            # Draw the circumference of the circle.
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

    cv2.imshow("Detected Circle", frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
