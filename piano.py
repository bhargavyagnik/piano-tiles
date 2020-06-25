import pyautogui as pg
from PIL import ImageGrab
import cv2
import numpy as np
import time

def up(sleep_time):
    time.sleep(sleep_time)
    pg.press("space")
    time.sleep(sleep_time)
    pg.press("down")

def boot():
    site = (345, 615, 775, 760)  # for google chrome
    while(True):
        printscreen_pil=ImageGrab.grab(bbox=site)
        im=cv2.cvtColor(np.array(printscreen_pil),cv2.COLOR_BGR2GRAY)
        #im=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
        lower_red = np.array([0])
        upper_red = np.array([50])
        mask = cv2.inRange(im, lower_red, upper_red)
        try:
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            areas = [cv2.contourArea(c) for c in contours]
            max_index = np.argmax(areas)
            cnt = contours[max_index]
            if areas[max_index] >= 12000 and areas[max_index] <= 16000:
                x, y, w, h = cv2.boundingRect(cnt)
                if w<=200 :
                    pg.click(345+x+(w/2),615+y+(h/2))
                    cv2.rectangle(im, (x, y), (x + w, y + h), (255), 5)
                    print(areas[max_index])
        except:
            print('error occured')
            #cv2.imshow('window',im1)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__=="__main__":
    boot()

