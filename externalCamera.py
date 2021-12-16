import time
import pyzbar.pyzbar as pyzbar
import cv2

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()


def startApp():
    global turnOn
    turnOn = True


def decode(img):
    numbers = ""
    decoded = pyzbar.decode(img)
    for obj in decoded:
        print('Type: ', obj.type)
        print('Data: ', obj.data.decode('utf-8'), '\n')
        numbers = obj.data.decode('utf-8')
    return numbers


startApp()
print("Start to read QR code")

while True:
    if turnOn == True:
        _, img = cap.read()
        data = decode(img)

        if data:
            turnOn = False
            print(data)
            data = ""

        cv2.imshow("camera", img)
    else:
        cap.read()
        # cv2.destroyAllWindows()
        time.sleep(5)
        turnOn = True

    if cv2.waitKey(1) == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()
