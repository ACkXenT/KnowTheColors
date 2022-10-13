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
            # меняем цветовую модель на HSV
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # отображаем кадр в окне с именем result
            cv2.imshow('result', img)
        except:
            cap.release()
            raise

        ch = cv2.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
