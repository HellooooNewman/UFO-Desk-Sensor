# Works but isn't accurate at a distance
# import the necessary packages
# include <opencv2/aruco.hpp>
from imutils import paths
import numpy as np
import imutils
import cv2
import cv2.aruco as aruco
import threading
import time

vid = cv2.VideoCapture(0)
areaDiff1 = 0
areaDiff2 = 0
starttime = time.time()


def calculateArea(corners):
    area = 0

    if(len(corners) > 0):

        point0 = corners[0][0][0]
        point1 = corners[0][0][1]
        point2 = corners[0][0][2]
        point3 = corners[0][0][3]

        # 0 = x
        # 1 = 1
        area = abs(
            (point0[0] + point1[1] - point0[1] + point1[0]) +
            (point1[0] + point2[1] - point1[1] + point2[0]) +
            (point2[0] + point3[1] - point2[1] + point3[0]) +
            (point3[0] + point0[1] - point3[1] + point0[0])
        )/2

        # for corner in corners:
        #     xDiff = corner[0][0] - corner[0][1]
        #     yDiff = corner[0][2] - corner[0][3]
        #     area = area + corner[0][1] * yDiff - corner[0][3] * xDiff

        # print("area" + str(area[0]))
        # area = 0.5 * area[0]

    return area


while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    areaDiff1 = areaDiff2
    time.sleep(0.3 - ((time.time() - starttime) % 0.3))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters)

    areaDiff2 = calculateArea(corners)

    newDiff = areaDiff1 - areaDiff2

    print(abs(newDiff))
    if abs(newDiff) > 5:
        frame = aruco.drawDetectedMarkers(gray, corners, ids)
        cv2.putText(frame, "Moving",
                    (frame.shape[1] - 400, frame.shape[0] -
                     20), cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (0, 255, 0), 3)

    # print("Diff = " + str(newDiff))

    cv2.imshow("Arucuno", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
