from operator import is_
import matplotlib.pyplot as plt
import pyautogui
import time
import pytesseract
from PIL import ImageOps
from send_sms import smsObject

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
OFFSET_LEFT, OFFSET_WIDTH, SAMPLE_RATE_IN_SEC = 110,50, 60*10



# get image location
loc = pyautogui.locateOnScreen('waitingServer.JPG', confidence=0.7)
if loc != None:
    img = pyautogui.screenshot(region = (loc.left + OFFSET_LEFT,loc.top, loc.width+ OFFSET_WIDTH,loc.height))
    # display number, if img looks good move on to sampling
    plt.imshow(img)
    plt.show()


    # get queue number every sample
    num_queue = int(pytesseract.image_to_string(ImageOps.grayscale(img)))
    # instantiate twilio client
    notifier = smsObject()
    notifier.createClient()
    notifier.setQueueNum(num_queue)
    notifier.sendMsg(is_init=True)
    print(num_queue)
    while(num_queue > 100):
        time.sleep(SAMPLE_RATE_IN_SEC)
        if loc != None:
            img = pyautogui.screenshot(region = (loc.left + OFFSET_LEFT,loc.top, loc.width+ OFFSET_WIDTH,loc.height))
            num_queue = int(pytesseract.image_to_string(ImageOps.grayscale(img)))
            notifier.setQueueNum(num_queue)
    notifier.sendMsg(is_init=False)   
            
else:
    print("'Waiting for Server' text box not detected")

