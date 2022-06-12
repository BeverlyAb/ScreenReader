# ScreenReader
 Reads queue number from Lost Ark and sends text notification when you are near the front of the line.
 
<!-- GETTING STARTED -->
## Getting Started
To bypass creating environments, a token.txt file is needed.
Create a token.txt file with the following id's and populate the X's with your values. _FROM_PHONE_ is the Twilio phone number and _TO_PHONE_ is the subscriber.

* TWILIO_ACCOUNT_SID XXXXXXXXXXXXXXXXXXXXXXXXX 
* TWILIO_AUTH_TOKEN XXXXXXXXXXXXXXXXXXXXXX
* FROM_PHONE +1XXXXXXX
* TO_PHONE +1XXXXXXX


<p align="right">(<a href="#top">back to top</a>)</p>


### Prerequisites

Download from Tesseract [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki). Ideally this should be saved under your Program Files.


### Installation

1. Python libraries
  ```sh
  pip install -r requirements.txt
  ```
2. Set up [https://www.twilio.com/try-twilio](Twilio) account and create a Twilio phone number.
3. Create your token.txt
   

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Run Lost Ark and take screenshot of the queue number and save it as `waitingServer.JPG`. Do not close the screenshot yet. 
2. Run the program
  ```s
  python screen_reader.py
  ```
  And close the screenshot image. 
  
3. A new image will appear and if the queue number is successfully shown, an init message will be sent to _TO_PHONE_. Once your queue number is less than 100, you will receive the final notification indicating that it is almost game time.  


Example of `waitingServer.JPG` ![Example of `waitingServer.JPG`](waitingServer.JPG)


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Continually reads the queue number every 10 min.
- [x] Can send sms msg
- [ ] Set path env
- [ ] Schedule Lost Ark and Screen Reader
- [ ] Optional
    - [ ] Move Mouse software

<p align="right">(<a href="#top">back to top</a>)</p>

