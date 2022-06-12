from operator import is_
import matplotlib.pyplot as plt
import pyautogui
import time
import pytesseract
from PIL import ImageOps
from send_sms import smsObject

DEBUG = True

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
OFFSET_LEFT, OFFSET_WIDTH, SAMPLE_RATE_IN_SEC = 0, 0, 60*1

# get image location
loc = pyautogui.locateOnScreen('waitingServer.JPG', confidence=0.7)
if loc != None:
    img = pyautogui.screenshot(region = loc)
    if pytesseract.image_to_string(ImageOps.grayscale(img)).strip().isdigit:
        num_queue = int(pytesseract.image_to_string(ImageOps.grayscale(img)))

    # instantiate twilio client
    notifier = smsObject()
    notifier.createClient()
    notifier.setQueueNum(num_queue)
    if not DEBUG: notifier.sendMsg(is_init=True)
    
    if DEBUG: print(num_queue)

    # get queue number every sample
    while(num_queue > 200):
        time.sleep(SAMPLE_RATE_IN_SEC)
        img = pyautogui.screenshot(region = loc)
        if pytesseract.image_to_string(ImageOps.grayscale(img)).strip().isdigit: 
            num_queue = int(pytesseract.image_to_string(ImageOps.grayscale(img)).strip())
            notifier.setQueueNum(num_queue)
        
        if DEBUG: print(num_queue)
    
    if not DEBUG: notifier.sendMsg(is_init=False)   
            
else:
    print("'Waiting for Server' text box not detected")

