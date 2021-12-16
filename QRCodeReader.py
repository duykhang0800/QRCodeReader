from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(img):
    #Detect QR code
    decoded = pyzbar.decode(img)
    #Print collected result for testing
    for obj in decoded:
            print('Type: ', obj.type)
            print('Data: ', obj.data.decode('utf-8'), '\n')
    return decoded

#Main
if __name__ == '__main__':
    window_name = 'image'
    img = cv2.imread('QR_codes/QR_text.png')
    decodedObjects = decode(img)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)