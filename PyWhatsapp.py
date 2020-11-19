import schedule
# Importing traceback to catch xml button not found errors in the future
import traceback
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

try:
    import autoit
except ModuleNotFoundError:
    pass
import time
import datetime
import os
import argparse
import platform

if platform.system() == 'Darwin':
    # MACOS Path
    chrome_default_path = os.getcwd() + '/driver/chromedriver'
else:
    # Windows Path
    chrome_default_path = os.getcwd() + '/driver/chromedriver.exe'

parser = argparse.ArgumentParser(description='PyWhatsapp Guide')
parser.add_argument('--chrome_driver_path', action='store', type=str, default=chrome_default_path,
                    help='chromedriver executable path (MAC and Windows path would be different)')
parser.add_argument('--message', action='store', type=str, default='', help='Enter the msg you want to send')
parser.add_argument('--remove_cache', action='store', type=str, default='False',
                    help='Remove Cache | Scan QR again or Not')
parser.add_argument('--import_contact', action='store', type=str, default='False',
                    help='Import contacts.txt or not (True/False)')
parser.add_argument('--enable_headless', action='store', type=str, default='False',
                    help='Enable Headless Driver (True/False)')
args = parser.parse_args()

if args.remove_cache == 'True':
    os.system('rm -rf User_Data/*')
browser = None
Contact = None
message = None if args.message == '' else args.message
Link = "https://web.whatsapp.com/"
wait = None
choice = None
docChoice = None
doc_filename = None
unsaved_Contacts = None


def input_contacts():
    global Contact, unsaved_Contacts
    # List of Contacts
    Contact = []
    unsaved_Contacts = []
    while True:
        # Enter your choice 1 or 2
        print("PLEASE CHOOSE ONE OF THE OPTIONS:\n")
        print("1.Message to Saved Contact number")
        print("2.Message to Unsaved Contact number\n")
        x = int(input("Enter your choice(1 or 2):\n"))
        print()
        if x == 1:
            n = int(input('Enter number of Contacts to add(count)->'))
            print()
            for i in range(0, n):
                inp = str(input("Enter contact name(text)->"))
                inp = '"' + inp + '"'
                # print (inp)
                Contact.append(inp)
        elif x == 2:
            n = int(input('Enter number of unsaved Contacts to add(count)->'))
            print()
            for i in range(0, n):
                # Example use: 919899123456, Don't use: +919899123456
                # Reference : https://faq.whatsapp.com/en/android/26000030/
                inp = str(input(
                    "Enter unsaved contact number with country code(interger):\n\nValid input: 91943xxxxx12\nInvalid input: +91943xxxxx12\n\n"))
                # print (inp)
                unsaved_Contacts.append(inp)

        choi = input("Do you want to add more contacts(y/n)->")
        if choi == "n":
            break

    if len(Contact) != 0:
        print("\nSaved contacts entered list->", Contact)
    if len(unsaved_Contacts) != 0:
        print("Unsaved numbers entered list->", unsaved_Contacts)
    input("\nPress ENTER to continue...")


def input_message():
    global message
    # Enter your Good Morning Msg
    print(
        "Enter the message and use the symbol '~' to end the message:\nFor example: Hi, this is a test message~\n\nYour message: ")
    message = []
    done = False

    while not done:
        temp = input()
        if len(temp) != 0 and temp[-1] == "~":
            done = True
            message.append(temp[:-1])
        else:
            message.append(temp)
    message = "\n".join(message)
    print(message)


def whatsapp_login(chrome_path, headless):
    global wait, browser, Link
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data')
    if headless == 'True':
        chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 600)
    browser.get(Link)
    browser.maximize_window()
    print("QR scanned")


def send_message(target):
    global message, wait, browser
    try:
        x_arg = '//span[contains(@title,' + target + ')]'
        ct = 0
        while ct != 5:
            try:
                group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()
                break
            except Exception as e:
                print("Retry Send Message Exception", e)
                ct += 1
                time.sleep(3)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfully")
        time.sleep(1)
    except NoSuchElementException as e:
        print("send message exception: ", e)
        return


def send_unsaved_contact_message():
    global message
    try:
        time.sleep(10)
        browser.implicitly_wait(10)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfully")
    except Exception as e:
        print("Failed to send message exception: ", e)
        return


def send_attachment():
    # Attachment Drop Down Menu
    try:
        clipButton = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
        clipButton.click()
    except:
        traceback.print_exc()
    time.sleep(1)

    # To send Videos and Images.
    try:
        mediaButton = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button')
        mediaButton.click()
    except:
        traceback.print_exc()
    time.sleep(3)
    hour = datetime.datetime.now().hour
    # After 5am and before 11am scheduled this.
    if (hour >= 5 and hour <= 11):
        image_path = os.getcwd() + "\\Media\\" + 'goodmorning.jpg'
    # After 9pm and before 11pm schedule this
    elif (hour >= 21 and hour <= 23):
        image_path = os.getcwd() + "\\Media\\" + 'goodnight.jpg'
    else:  # At any other time schedule this.
        image_path = os.getcwd() + "\\Media\\" + 'howareyou.jpg'
    # print(image_path)

    autoit.control_focus("Open", "Edit1")
    autoit.control_set_text("Open", "Edit1", image_path)
    autoit.control_click("Open", "Button1")

    time.sleep(3)
    # Send button
    try:
        whatsapp_send_button = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
        whatsapp_send_button.click()
    except:
        traceback.print_exc()
    
    print("File sent")


def send_files():
    global doc_filename
    # Attachment Drop Down Menu
    clipButton = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
    clipButton.click()
    
    time.sleep(1)
    # To send a Document(PDF, Word file, PPT)
    # This makes sure that gifs, images can be imported through documents folder and they display
    # properly in whatsapp web.
    if doc_filename.split('.')[1]=='pdf'or doc_filename.split('.')[1]=='docx'or doc_filename.split('.')[1]=='pptx' :
        try:
            docButton = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[3]/button')
            
            docButton.click()
        except:
            # Check for traceback errors with XML imports
            traceback.print_exc()
    else:
        try: 
            # IMG attatchment button
            docButton = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button')
            docButton.click()
        except:
            # Check for traceback errors with XML imports
            traceback.print_exc()
    time.sleep(1)
    docPath = os.getcwd() + "\\Documents\\" + doc_filename
    try:
        autoit.control_focus("Open", "Edit1")
    except :
        traceback.print_exc()
    autoit.control_set_text("Open", "Edit1", (docPath))
    autoit.control_click("Open", "Button1")
    time.sleep(3)
    # Changed whatsapp send button xml link.
    whatsapp_send_button = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')

    whatsapp_send_button.click()
    print('File sent')

def import_contacts():
    global Contact, unsaved_Contacts
    Contact = []
    unsaved_Contacts = []
    fp = open("contacts.txt", "r")
    while True:
        line = fp.readline()
        con = ' '.join(line.split())
        if con and con.isdigit():
            unsaved_Contacts.append(int(con))
        elif con:
            Contact.append(con)
        if not line:
            break


def sender():
    global Contact, choice, docChoice, unsaved_Contacts
    print(Contact, unsaved_Contacts)
    for i in Contact:
        try:
            send_message(i)
            print("Message sent to ", i)
        except Exception as e:
            print("Msg to {} send Exception {}".format(i, e))
        if (choice == "yes"):
            try:
                send_attachment()
            except:
                print('Attachment not sent.')
        if (docChoice == "yes"):
            try:
                send_files()
            except:
                print('Files not sent')
    time.sleep(5)
    if len(unsaved_Contacts) > 0:
        for i in unsaved_Contacts:
            link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(i)
            # driver  = webdriver.Chrome()
            browser.get(link)
            print("Sending message to", i)
            send_unsaved_contact_message()
            if (choice == "yes"):
                try:
                    send_attachment()
                except:
                    print()
            if (docChoice == "yes"):
                try:
                    send_files()
                except:
                    print()
            time.sleep(7)


# For GoodMorning Image and Message
schedule.every().day.at("07:00").do(sender)
# For How are you message
schedule.every().day.at("13:35").do(sender)
# For GoodNight Image and Message
schedule.every().day.at("22:00").do(sender)

# Example Schedule for a particular day of week Monday
schedule.every().monday.at("08:00").do(sender)


# To schedule your msgs
def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    print("Web Page Open")

    if os.path.exists("contacts.txt") and args.import_contact == 'True':
        # read contacts from text file
        import_contacts()
    if not Contact and not unsaved_Contacts:
        # Append more contact as input to send messages
        input_contacts()
    if message == None:
        # Enter the message you want to send
        input_message()

    # If you want to schedule messages for
    # a particular timing choose yes
    # If no choosed instant message would be sent
    isSchedule = input('Do you want to schedule your Message(yes/no):')
    if (isSchedule == "yes"):
        jobtime = input('input time in 24 hour (HH:MM) format - ')

    # Send Attachment Media only Images/Video
    choice = input("Would you like to send attachment(yes/no): ")

    docChoice = input("Would you file to send a Document file(yes/no): ")
    if (docChoice == "yes"):
        # Note the document file should be present in the Document Folder
        doc_filename = input("Enter the Document file name you want to send: ")

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login(args.chrome_driver_path, args.enable_headless)

    # Send message to all Contact List
    # This sender is just for testing purpose to check script working or not.
    # Scheduling works below.
    if isSchedule == "yes":
        schedule.every().day.at(jobtime).do(sender)
    else:
        sender()
        print("Task Completed")

    # Messages are scheduled to send
    # Default schedule to send attachment and greet the personal
    # For GoodMorning, GoodNight and howareyou wishes
    # Comment in case you don't want to send wishes or schedule
    scheduler()
    # browser.quit()
