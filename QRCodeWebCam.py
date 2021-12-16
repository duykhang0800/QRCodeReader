import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time

# Change the index number according to camera
cap = cv2.VideoCapture(0)

cap.set(3, 460)
cap.set(4, 480)
# time.sleep(10)

def decode(img):
    # Detect QR code
    decoded = pyzbar.decode(img)
    # Print collected result for testing
    for obj in decoded:
        print('Type: ', obj.type)
        print('Data: ', obj.data.decode('utf-8'), '\n')
    return decoded

while cap.isOpened():
    # Capture the img from the camera frame by frame
    ret, frame = cap.read()
    cv2.imshow('Video', frame)
    # cap.release()
    # Pass the frame into the decode function
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    decodedObj = decode(img)
    # time.sleep(5)

    if cv2.waitKey(10) & 0xFF == ord('b'):
        break

cap.release()
cv2.destroyAllWindows()