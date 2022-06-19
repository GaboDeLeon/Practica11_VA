import cv2
import numpy as np

imagen_1 = cv2.imread("windows_1.jpg")
imagen2 = cv2.imread("windows_2.jpg")

imagen1 = cv2.resize(imagen_1, dsize=(450,280),interpolation=cv2.INTER_CUBIC)

cv2.imshow("imagen_1",imagen1)
cv2.imshow("imagen_2",imagen2)

def comparacion(imagen1,imagen2):
    diferencia=cv2.subtract(imagen1,imagen2)
    if not np.any(diferencia):
        print("Las imagenes son iguales")
    else:
        print("Las imagenes son diferentes")
        cv2.imwrite("dif.jpg",diferencia)
        cv2.imshow("diferencia",diferencia)

comparacion(imagen1,imagen2)



