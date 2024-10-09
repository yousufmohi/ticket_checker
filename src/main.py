from ticket_checker import reCheck, setupBrowser, quit
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    driver = setupBrowser()

    senderEmail = os.getenv("EMAIL")
    senderPassword = os.getenv("PASSWORD")
    recepient = os.getenv('RECEPIENT')
    link = os.getenv('Link')
    try:
        reCheck(driver=driver,link=link,senderEmail=senderEmail,senderPassword=senderPassword,recepient=recepient)
    except KeyboardInterrupt:
        print("Script stopped by keyboard interrupt")
    finally:
        quit(driver=driver)
    

if __name__ == "__main__":
    main()