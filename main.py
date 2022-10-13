#import sys
import cv2 as cv
import numpy as np

hsv_min = np.array((21, 28, 65), np.uint8)
hsv_max = np.array((255, 250, 255), np.uint8)

cap = cv.VideoCapture(0)


if __name__ == '__main__':
    print(__doc__)
    cv.namedWindow("frame")
    while(True):
        ret, frame = cap.read()
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    #photo = r'C:\Users\i301\Downloads\1612281880_93-p-zvezdochki-na-fioletovom-fone-122.png'
    #img = cv.imread(photo)
    #hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    #tresh = cv.inRange(hsv, hsv_min, hsv_max)
    #contours, hierarchy = cv.findContours(tresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #cv.drawContours(img, contours, -1, (50, 0, 200), 40, cv.LINE_AA, hierarchy, 1)
    #cv.imshow('contours', img)

    #cv.drawContours(img, contours, -1, (200, 50, 50), 25, cv.LINE_AA, hierarchy, 1)
    #cv.imshow('contours', img)

    #cv.drawContours(img, contours, -1, (255, 255, 255), 5, cv.LINE_AA, hierarchy, 1)
    #cv.imshow('contours', img)

    cv.waitKey(0)
    cap.release()
    cv.destroyAllWindows()



#img = cv2.imread(r'C:\Users\i301\Downloads\cat.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2SHV)
#cv2.namedWindow("POPCAT")
#cv2.imshow("POPCAT", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()