# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2

FOCAL_LENGTH = 906.107
RADIUS_OF_MARKER = 2.2
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
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    cv2.imshow('edged', edged)

    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)

    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c), cnts


def distance_to_camera(rad):
    # compute and return the distance from the maker to the camera
    return str((FOCAL_LENGTH * RADIUS_OF_MARKER) / rad)


while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # load the image, find the marker in the image, then compute the
    # distance to the marker from the camera
    marker, contour = find_marker(frame)

    # draw a bounding box around the image and display it
    box = cv2.cv.BoxPoints(
        marker) if imutils.is_cv2() else cv2.boxPoints(marker)
    box = np.int0(box)

    # Find cirlce cneter
    (x, y), radius = cv2.minEnclosingCircle(box)
    # center = (int(x), int(y))
    # radius = int(radius)

    cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
    area = cv2.contourArea(contour[0])
    if isPixelRed(frame, x, y):
        # print(area)
        if area > 20:
            dText = "Distance: " + distance_to_camera(radius)
            aText = "Area: " + str(area)
            cv2.putText(frame, aText,
                        (frame.shape[1] - 400, frame.shape[0] -
                         40), cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0), 3)
            cv2.putText(frame, dText,
                        (frame.shape[1] - 400, frame.shape[0] -
                         20), cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
