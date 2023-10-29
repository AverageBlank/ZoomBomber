# Starting of the program
############## ! Imports ##############
# ? Selenium --> For interacting with the web browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

# ? Time --> For pausing the program
from time import sleep

# ? Questionary --> For beautiful command line prompts
from questionary import Style, select, text

# ? PyAutoGUI --> For preventing zoom popup
from pyautogui import keyDown, click, locateCenterOnScreen

# ? OS --> For clearing the screen
from os import system, name as OSNAME

# ? Rich --> For a box and loading bar
from rich import print
from rich.console import Console

console = Console()
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
)
from rich.align import Align


############## ! Functions ##############
# * Initializing selenium with Chrome settings
def setSelenium():
    global allNames, chromeOptions
    chromeOptions = ChromeOptions()
    chromeOptions.add_experimental_option("detach", True)
    chromeOptions.add_argument("--use-fake-ui-for-media-stream")

    # ? Reading all the names from 'names.txt'
    allNames = open("names.txt", "r").read().split("\n")


# * Clicking join from browser on the page
def clickJoinFromBrowser():
    try:
        # ? Searches for the join browser button to click onto
        x, y = locateCenterOnScreen("join_browser.png")
        click(x, y)
    except Exception as e:
        print("Error handling Zoom prompt:", str(e))


# * Function if user selected ID and Password method
def idPass(id=None, password=None):
    # ? If ID is not provided
    if id == None:
        id = text("Enter Zoom Meeting ID:", style=minimalStyle).ask().replace(' ', '')

    else:
        # ? If ID is provided
        id = int(str(id.replace(" ", "")))

    # ? If password is not provided
    if password == None:
        password = text("Enter Zoom Meeting Password:", style=minimalStyle).ask()

    # ? Creating a loop for all the names provided
    for name in allNames:
        driver = webdriver.Chrome(options=chromeOptions)
        # ? Opening the website
        driver.get(
            f"https://zoom.us/wc/{id}/join?from=join&_x_zm_rtaid=ws81SA1uSGuB2O6_Sekbbg.1690523013218.d0e8a870b0195ee064d41de484bdd657&_x_zm_rhtaid=508"
        )
        sleep(0.5)

        # ? Entering password
        pwd = driver.find_element(By.ID, "input-for-pwd")
        pwd.clear()
        pwd.send_keys(password)

        # ? Entering name
        user = driver.find_element(By.ID, "input-for-name")
        user.clear()
        user.send_keys(name)

        # ? Joining audio and muting mic
        audioButton = driver.find_element(By.ID, "preview-audio-control-button")
        audioButton.click()
        sleep(0.1)
        audioButton2 = driver.find_element(By.ID, "preview-audio-control-button")
        audioButton2.click()
        user.send_keys(Keys.RETURN)


# * Function if user selected link method
def link(link=None):
    # ? If link is not provided
    if link == None:
        link = text("Enter Zoom Meeting Link:", style=minimalStyle).ask() + "#success"

    # ? Creating a loop for all the names provided
    for name in allNames:
        # ? Opening the browser
        driver = webdriver.Chrome(options=chromeOptions)

        # ? Opening the website
        driver.get(link)

        # ? Bypassing prompt to open zoom in the browser
        launchApp = driver.find_element(By.CLASS_NAME, "mbTuDeF1")
        launchApp.click()
        sleep(0.5)
        clickJoinFromBrowser()

        # ? Entering name
        sleep(5)
        user = driver.find_element(By.ID, "input-for-name")
        user.clear()
        user.send_keys(name)

        # ? Joining audio and muting mic
        audioButton = driver.find_element(By.ID, "preview-audio-control-button")
        audioButton.click()
        sleep(0.1)
        audioButton2 = driver.find_element(By.ID, "preview-audio-control-button")
        audioButton2.click()
        user.send_keys(Keys.RETURN)


# * Loading Bar
def StatBar(time: float, desc: str):
    progress_bar = Progress(
        TextColumn(f"{desc} "),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    with progress_bar as p:
        for i in p.track(range(100), description=desc):
            sleep(time / 100)
    sleep(0.5)


############## ! Printing Options ##############
if __name__ == "__main__":
    setSelenium()
    system("clear" if OSNAME == 'posix' else "cls")
    Align.center(
        StatBar(2, desc="[cyan]Loading Zoom Bomber"), vertical="middle"
    )
    system("clear" if OSNAME == 'posix' else "cls")
    console.print(
        Panel.fit("[bold italic #77DDD4]Zoom Bomber", padding=(0, 22))
    )
    minimalStyle = Style(
        [
            ("answer", "fg:#FFFFFF italic"),  # ? White
            ("question", "fg:#FFFFFF bold"),  # ? White
            ("pointer", "fg:#00FFFF bold"),  # ? Cyan
            ("highlighted", "fg:#FFFFFF"),  # ? White
            ("selected", "fg:#A9A9A9"),  # ? Grey
            ("qmark", "fg:#77DD77"),  # ? Green
        ]
    )
    userSelect = select(
        "Choose a way to bomb your meetings: ", ["ID/Pass", "Link"], style=minimalStyle
    ).ask()
    sleep(0.5)
    system("clear" if OSNAME == 'posix' else "cls")
    if userSelect == "ID/Pass":
        idPass()
    elif userSelect == "Link":
        link()
    else:
        print("Unknown error, please restart the program")
