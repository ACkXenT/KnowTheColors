import cv2

if __name__ == '__main__':
    # создаем окно с именем result
    cv2.namedWindow("result")

    # создаем объект cap для захвата кадров с камеры
    cap = cv2.VideoCapture(0)

    while True:
        # захватываем текущий кадр и кладем его в переменную img
        flag, img = cap.read()
        try:
            # размываем кадр
            img = cv2.GaussianBlur(img, (5, 5), 2)
            # отображаем кадр в окне с именем result
            cv2.imshow('result', img)
        except:
            cap.release()
            raise

        ch = cv2.waitKey(5)
        if ch == 27:
            break
