import cv2
import numpy as NotImplemented

cap = cv2.VideoCapture(0)
ftype = "Original"
print("r=Red, g=Green, b=Blue, s=Sobel, c=Canny, t=Cartoon, o=Original, q=Quit")

def apply_filter(img, ftype):
    if ftype == "red":
        img[:, :, 0] = 0  #blue
        img[:, :, 1] = 0  #green

    elif ftype == "green":
        img[:, :, 0] = 0  #blue
        img[:, :, 2] = 0  #red

    elif ftype == "blue":
        img[:, :, 1] = 0  #green
        img[:, :, 2] = 0  #red   

    elif ftype == "Sobel":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.Sobel(gray, cv2.CV_8U, 1,1)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    elif ftype == "Canny":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)         

    elif ftype == "Cartoon":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edge = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(img, 9, 250, 250)
        img = cv2.bitwise_and(color, color, mask=edge)

    return img


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if ftype == "Original":
        output = frame
    else:
        output = apply_filter(frame.copy(), ftype)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
      ftype = "red"
    elif key == ord('g'):
        ftype = "green"
    elif key == ord('b'):
        ftype = "blue"
    elif key == ord('s'):
        ftype = "sobel"
    elif key == ord('c'):
        ftype = "canny"
    elif key == ord('t'):
        ftype = "cartoon"
    elif key == ord('o'):
        ftype = "original"
    elif key == ord('q'):
     break

    cv2.imshow("Filter" , output)

cap.release()
cv2.destroyAllWindows()