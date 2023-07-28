# Starting of the program
############## ! Imports ##############
# ? Selenium --> For interacting with the web browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
# ? Time --> For pausing the program
from time import sleep


############## ! Setting Up Selenium ##############
chromeOptions = ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
chromeOptions.add_argument("--use-fake-ui-for-media-stream")


############## ! The Bomber ##############
# ? Reading all the names from 'names.txt'
allNames = open("names.txt", "r").read().split('\n')

def bomber(id=None, password=None):
    # ? If ID is not provided
    if id == None:
        id = int(input("Enter Zoom ID: ").replace(" ", ""))
    else:
        # ? If ID is provided
        id = int(str(id.replace(" ", "")))
    # ? If password is not provided
    if password == None:
        password = input("Enter Zoom password: ")

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
        sleep(0.25)
        audioButton2 = driver.find_element(By.ID, "preview-audio-control-button")
        audioButton2.click()
        user.send_keys(Keys.RETURN)


if __name__ == "__main__":
    bomber()
