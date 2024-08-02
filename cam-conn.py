import requests
import cv2
import numpy as np
from requests.auth import HTTPBasicAuth
import imutils
from time import sleep

# URL given by the camera.
url = input('Enter camera URL.')
url += 'shot.jpg'
user = input('test only ofc. Enter username')
passw = input('test only ofc. Enter psw')


while True:
    # to lag the video
    # sleep(2)
    img_response = requests.get(url, auth=HTTPBasicAuth(user, passw))
    # img to array
    img = np.array(bytearray(img_response.content), dtype=np.uint8)
    # array to image
    image = cv2.imdecode(img, -1)
    image = imutils.resize(image, width=800, height=600)
    cv2.imshow("RoberCamera", image)

    # Press esc to kill camera
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
