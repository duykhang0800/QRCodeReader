import time
import pyzbar.pyzbar as pyzbar
import cv2
import asyncio
import requests
import json

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
link = "http://52.76.27.252:3000/registrations/verify/"


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


def fetch_and_check(data):
    get_api = link + str(data)
    response = requests.get(get_api)
    # response.json()
    parse_json = json.loads(response.text)
    # print(response.text)
    # print(parse_json)
    # print(parse_json["valid"])
    if parse_json['valid'].lower() == 'yes':
        print("Access granted")
    else:
        if parse_json['valid'].lower() == 'no':
            print("Access denied")
        else:
            print("Invalid response")
    return response


startApp()
print("Start to read QR code")

while True:
    if turnOn == True:
        _, img = cap.read()
        data = decode(img)

        if data:
            turnOn = False
            print(data)
            fetch_and_check(data)
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
