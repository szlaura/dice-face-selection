import cv2
import numpy as np

ptsLst = []
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])


def point_matching():
    global ptsLst

    if len(ptsLst) >= 4:
        pts1 = np.float32(ptsLst).reshape(-1, 1, 2)
        matrix = cv2.getPerspectiveTransform(pts1, pts2)

        if matrix is None:
            print('No solution found!')
        else:
            dst = cv2.warpPerspective(clone, matrix, (300, 300))
            cv2.imshow('Dice face', dst)


def mouse_click(event, x, y, flags, param):
    global ptsLst, image

    if event == cv2.EVENT_LBUTTONUP:
        ptsLst.append((x, y))
        point_matching()
        cv2.drawMarker(image, (x, y), (0, 255, 0), cv2.MARKER_TILTED_CROSS)
        cv2.imshow('Dice face detection', image)


image = cv2.imread('dice.png')
clone = image.copy()
cv2.namedWindow('Dice face detection')
cv2.setMouseCallback('Dice face detection', mouse_click)

cv2.imshow('Dice face detection', image)
key = cv2.waitKey()
cv2.destroyAllWindows()
