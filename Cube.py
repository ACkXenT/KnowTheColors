import cv2
import numpy as np

if __name__ == '__main__':
    cv2.namedWindow("result")
    cap = cv2.VideoCapture(0)

    hsv_min = np.array((0, 200, 60), np.uint8) #красный, оранжевый и жёлтый
    hsv_max = np.array((50, 250, 250), np.uint8)

    hsv_min1 = np.array((80, 50, 40), np.uint8) #зелёный
    hsv_max1 = np.array((130, 250, 250), np.uint8)

    hsv_min2 = np.array((160, 40, 70), np.uint8) #синий и фиолетовый
    hsv_max2 = np.array((215, 250, 250), np.uint8)

    color_purple = (250, 0, 160)
    color_green = (0, 250, 90)

    color_red = (0, 90, 250)
    color_blue = (250, 128, 14)

    color_yellow = (50, 250, 250)
    color_orange = (0, 90, 250)

    while True:
        flag, img = cap.read()
        img = cv2.flip(img, 1)
        try:
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            thresh = cv2.inRange(hsv, hsv_min, hsv_max)
            contours0, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            for cnt in contours0:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                center = (int(rect[0][0]), int(rect[0][1]))
                area = int(rect[1][0]*rect[1][1])

                edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
                edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

                usedEdge = edge1
                if cv2.norm(edge2) > cv2.norm(edge1):
                    usedEdge = edge2

                reference = (1, 0)

                if area > 500:
                    cv2.drawContours(img, [box], 0, color_purple, 2)
                    cv2.circle(img, center, 5, color_green, 2)
                    cv2.putText(img, 'red', (center[0]+20, center[1]-20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, color_green, 2)
            cv2.imshow('result', img)

            thresh1 = cv2.inRange(hsv, hsv_min1, hsv_max1)
            contours0, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            for cnt in contours0:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                center = (int(rect[0][0]), int(rect[0][1]))
                area = int(rect[1][0] * rect[1][1])

                edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
                edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

                usedEdge = edge1
                if cv2.norm(edge2) > cv2.norm(edge1):
                    usedEdge = edge2

                reference = (1, 0)

                if area > 500:
                    cv2.drawContours(img, [box], 0, color_red, 2)
                    cv2.circle(img, center, 5, color_blue, 2)
                    cv2.putText(img, 'green', (center[0]+20, center[1]-20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, color_blue, 2)
            cv2.imshow('result', img)

            thresh2 = cv2.inRange(hsv, hsv_min2, hsv_max2)
            contours0, hierarchy = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            for cnt in contours0:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                center = (int(rect[0][0]), int(rect[0][1]))
                area = int(rect[1][0] * rect[1][1])

                edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
                edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

                usedEdge = edge1
                if cv2.norm(edge2) > cv2.norm(edge1):
                    usedEdge = edge2

                reference = (1, 0)

                if area > 500:
                    cv2.drawContours(img, [box], 0, color_yellow, 2)
                    cv2.circle(img, center, 5, color_orange, 2)
                    cv2.putText(img, 'blue', (center[0] + 20, center[1] - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, color_orange, 2)
            cv2.imshow('result', img)

        except:
            cap.release()
            raise
        ch = cv2.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
