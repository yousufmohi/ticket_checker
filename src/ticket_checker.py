import time
import logging
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import exit


logging.basicConfig(filename="logs\\ticket_checker.log", level=logging.INFO)

def logMessage(message):
    logging.info(message)
    print(message)

def sendEmail(message,senderEmail,senderPassword, recepient,movie):
    text = f"Subject: Tickets are available!\n\nThe tickets for the movie are available."
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(senderEmail, senderPassword)
    server.sendmail(senderEmail, recepient, text)
def setupBrowser():
    # Set up Selenium with a headless browser (optional)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    return driver

def loadPage(driver: webdriver, link):
    driver.get(link)

def findButton(driver: webdriver, senderEmail,senderPassword,recepient):
    try:
        print("Checking for Tickets")
        ticket_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Get Tickets')]"))
        )
        if ticket_button:
            logMessage("Tickets are available")
            sendEmail("Tickets are Available!",senderEmail=senderEmail,senderPassword=senderPassword,recepient=recepient,movie="Joker 2")
            quit(driver=driver)
            exit(0)
    except NoSuchElementException:
        logMessage("Tickets are not available yet.")
    except TimeoutException:
        logMessage("Timed out waiting for the page to load or button to appear.")

# Find the button by its text
def quit(driver: webdriver):
    # Close the browser
    driver.quit()

def reCheck(driver: webdriver, link, senderEmail,senderPassword,recepient,interval = 50):

    while True:
        loadPage(driver=driver, link=link)
        findButton(driver=driver,senderEmail=senderEmail,senderPassword=senderPassword,recepient=recepient)
        print(f"Retrying in {interval/60} minutes...")
        time.sleep(interval)
