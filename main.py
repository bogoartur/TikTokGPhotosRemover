from PIL import ImageGrab
import os
import numpy as np
import cv2 as cv
import pygetwindow as gw
import time
import pytesseract
import pyautogui as pgui

win = gw.getWindowsWithTitle('Opera')[0]
win.activate()
time.sleep(0.7)
cascade = cv.CascadeClassifier('cascade/cascade.xml')
contador = 2800


def screensave_find():
    global contador
    filecont = 0
    box = (300, 65, 1050, 800)
    filepath = 'Screenshots/'
    for path in os.scandir(filepath):
        if path.is_file():
            filecont += 1
    screenshot = ImageGrab.grab(box)
    screenshot.save('Screenshots/screen.png', 'PNG')
    time.sleep(0.2)
    img = cv.imread('Screenshots/screen.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    tiktok = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    quantas = len(tiktok)
    
    if quantas == 1:
        
        pgui.leftClick(2117, 100)
        time.sleep(0.5)
        pgui.leftClick(2000, 300)
        time.sleep(0.1)
        pgui.leftClick(2000, 390)
        print("Eu já deletei ", contador, "TikToks.")
        contador += 1
        for (x, y, w, h) in tiktok:
            cv.rectangle(img, (x,y), (x+w, y+h), (0,0,200), thickness=2)
            cv.imshow("Detectado", img)
            cv.waitKey(500)
    elif quantas == 0:
        time.sleep(2)
        if quantas == 1:
        
            pgui.leftClick(2117, 100)
            time.sleep(0.5)
            pgui.leftClick(2000, 300)
            time.sleep(0.1)
            pgui.leftClick(2000, 390)
            print("Eu já deletei ", contador, "TikToks.")
            contador += 1
            for (x, y, w, h) in tiktok:
                cv.rectangle(img, (x,y), (x+w, y+h), (0,0,200), thickness=2)
                cv.imshow("Detectado", img)
                cv.waitKey(500)
        else:
            pgui.leftClick(2145, 550)
            time.sleep(0.3)
    else:
        pgui.leftClick(2145, 550)
        time.sleep(0.3)







while(True):
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    else:
        screensave_find()
        time.sleep(0.5)


#cv.rectangle(img, (100,100), (400,450), (0,0,200), thickness=2)
#cv.putText(img, "TikTok", (105,90), cv.FONT_HERSHEY_PLAIN, 1.0, (0,0,200))

#canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny', canny)

#cv.imwrite(('Screenshots/screen' + str(filecont) + '.jpg'), retangulado)
#cv.imshow('screen', gray)
