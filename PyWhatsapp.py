import schedule
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = None
Contact = None
message = None
Link = "https://web.whatsapp.com/"
wait = None

def input_contacts():
    global Contact
    Contact = ['"Shaurya"', '"Swadha"']
    n = int(input('Enter number of Contacts to add->'))
    for i in range(0,n):
        inp = str(input("Enter contact name->"))
        Contact.append(inp)


def input_message():
    global message
    # Enter your Good Morning Msg
    message = input("Enter the msg to send->")

def whatsapp_login():
    global wait,browser,Link
    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
    wait = WebDriverWait(browser, 600)
    browser.get(Link)
    browser.maximize_window()
    print("QR scanned")

def send_message(target):
    global message,wait, browser
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(1)

def sender():
    global Contact
    for i in Contact:
        send_message(i)

schedule.every().Monday.at("06:00").do(sender)
schedule.every().Tuesday.at("07:00").do(sender)
schedule.every().Friday.at("07:30").do(sender)
schedule.every().day.at("23:30").do(sender)

# To schedule your msgs
def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    print("Web Page Open")
    # Append more contact as input to send messages
    input_contacts()
    # Enter the message you want to send
    input_message()
    # Let us login and Scan
    whatsapp_login()
    # Send message to all Contact List
    sender()
    # First send Task Complete
    print("Completed")
    # Messages are scheduled to send
    scheduler()
    # browser.quit()