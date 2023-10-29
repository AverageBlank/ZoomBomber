## **ZoomBomber**
Zoom Bomber is a project I've dedicated time to as a way of learning a web-driver package called Selenium. The idea was inherently to join zoom meetings with provided links and/or ID & Password pair that opens multiple browser instances using Selenium to exploit the "Join With Browser" functionality in the Zoom webapp.
- FOR **EDUCATIONAL PURPOSES ONLY** (Please use it at your own risk)

## **Requirements:**
* Below are the python libraries used for running the program, you can either of the code blocks to download all the libraries.
```
pip install selenium
pip install pyautogui
pip install questionary
pip install rich
```
```
pip install -r libraries.txt
```

## **How It Works**
- The program using the `Selenium` web-driver and Python library for the same, exploits a vulnerability in Zoom's webapp that let's a user join a meeting without needing an account.
- It uses the `.png` files to locate the buttons required to click and uses `pyautogui` to navigate to the given button automatically.
- Given the names in the text file, it proceeds to launch an instance of a web-driver and fill the required details to joining the meeting automatically.
- It proceeds to mute audio to prevent an audio loop or unnecessary transfer of microphone audio into the meeting, giving you control over each of the web instances.
- Change names in `names.txt` which will be used in the meeting.
- Example in `names.txt`
  
## **Probable Fixes**
- **Chrome:** Have Chrome browser installed as the program is based on chrome web-drivers
- **ChromeDrivers [Optional]:**
   - In certain conditions, the ChromeDriver seems to be optional, so if you're having problems with running the program, installing them would help.
