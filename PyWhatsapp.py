import schedule
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import autoit
import time
import datetime
import os

browser = None
Contact = None
message = None
Link = "https://web.whatsapp.com/"
wait = None
choice = None

def input_contacts():
    global Contact
    # List of Contacts
    Contact = []
    n = int(input('Enter number of Contacts to add->'))
    for i in range(0,n):
        inp = str(input("Enter contact name->"))
        inp = '"' + inp + '"'
        # print (inp)
        Contact.append(inp)
    # Print the new Contact list after additional input contacts
    print(Contact)
    print('')


def input_message():
    global message
    # Enter your Good Morning Msg
    message = input("Enter the msg to send->")

def whatsapp_login():
    global wait,browser,Link
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 600)
    browser.get(Link)
    browser.maximize_window()
    print("QR scanned")

def send_message(target):
    global message,wait, browser
    try:
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        input_box.send_keys(message + Keys.ENTER)
        time.sleep(1)
    except NoSuchElementException:
        return

def send_attachment():
    # Attachment Drop Down Menu
    clipButton = browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clipButton.click()
    time.sleep(1)
    
    # To send Videos and Images.
    mediaButton = browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
    mediaButton.click()
    time.sleep(3)
    
    hour = datetime.datetime.now().hour
    
    # After 5am and before 11am scheduled this.
    if(hour >=5 and hour <=11):
        image_path = os.getcwd() +"\\Media\\" + 'goodmorning.jpg'
    # After 9pm and before 11pm schedule this
    elif (hour>=21 and hour<=23):
        image_path = os.getcwd() +"\\Media\\" + 'goodnight.jpg'
    else: # At any other time schedule this.
        image_path = os.getcwd() +"\\Media\\" + 'howareyou.jpg'
    # print(image_path)
    
    autoit.control_focus("Open","Edit1")
    autoit.control_set_text("Open","Edit1",(image_path) )
    autoit.control_click("Open","Button1")
    
    time.sleep(3)
    whatsapp_send_button = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
    whatsapp_send_button.click()
    


def sender():
    global Contact,choice
    for i in Contact:
        send_message(i)
        print("Message sent to ",i)
        if(choice=="yes"):
            send_attachment()

# For GoodMorning Image and Message
schedule.every().day.at("07:00").do( sender )
# For How are you message 
schedule.every().day.at("17:00").do( sender )
# For GoodNight Image and Message 
schedule.every().day.at("22:00").do( sender )

# Example Schedule for a particular day of week Monday
schedule.every().monday.at("08:00").do(sender) 


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
    #Send Attachment Media only Images/Video
    choice = input("Would you like to send attachment(yes/no): ")
    # Let us login and Scan
    whatsapp_login()
       
    # Send message to all Contact List
    # This sender is just for testing purpose to check script working or not.
    # Scheduling works below.
    #Comment this line is case you don't want to test 
    #or have completed the testing part of script.
    sender()
    
    # First send Task Complete
    print("Completed")
    
    # Messages are scheduled to send
    scheduler()
    
    # browser.quit()
    