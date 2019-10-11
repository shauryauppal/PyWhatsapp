import time, os, datetime, schedule

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

class PyWhatsApp:
    def __init__(self, link="https://web.whatsapp.com/", *args, **kwargs):
        self.browser = None
        self.contact = None
        self.message = None
        self.wait = None
        self.choice = None
        self.docChoice = None
        self.doc_filename = None
        self.unsaved_contacts = None

    def input_contacts(self):
        # List of Contacts
        self.contact = []
        self.unsaved_contacts = []
        
        while True:
            # Enter your choice 1 or 2
            print("PLEASE CHOOSE ONE OF THE OPTIONS:\n")
            print("1.Message to Saved Contact number")
            print("2.Message to Unsaved Contact number\n")
            choice = int(input("Enter your choice(1 or 2):\n"))
            print()
            if choice == 1:
                num_of_contacts = int(input('Enter number of Contacts to add(count)->'))
                print()
                for num in range(0, num_of_contacts):
                    contact_name = str(input("Enter contact name(text)->"))
                    contact_number = '"' + contact_name + '"'
                    self.contact.append(contact_name)
            elif choice == 2:
                num_of_unsaved_contacts = int(input('Enter number of unsaved Contacts to add(count)->'))
                print()
                for num in range(0, num_of_unsaved_contacts):
                    # Echoicexample use: 919899123456, Don't use: +919899123456
                    # Reference : https://faq.whatsapp.com/en/android/26000030/
                    contact_number = str(input("Enter unsaved contact number with country code(interger):\n\nValid input: 91943xxxxx12\nInvalid input: +91943xxxxx12\n\n"))
                    self.unsaved_contacts.append(contact_number)

            choice = input("Do you want to add more contacts(y/n)->")
            if choice == "n":
                break

        if len(self.contact) != 0:
            print("\nSaved contacts entered list->", self.contact)
        if len(self.unsaved_contacts) != 0:
            print("Unsaved numbers entered list->", self.unsaved_contacts)
        input("\nPress ENTER to continue...")

    def input_message(self):
        # Enter your Good Morning Msg
        print()
        print("Enter the message and use the symbol '~' to end the message:\nFor example: Hi, this is a test message~\n\nYour message: ")
        self.message = []
        temp = ""
        done = False

        while not done:
            temp = input()
            if len(temp) != 0 and temp[-1] == "~":
                done = True
                self.message.append(temp[:-1])
            else:
                self.message.append(temp)
        self.message = "\n".join(self.message)
        print()
        print(self.message)

    def whatsapp_login(self):
        chrome_options = Options()
        chrome_options.add_argument('--user-data-dir=./User_Data')
        self.browser = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.browser, 600)
        browser.get(self.link)
        browser.maximize_window()
        print("QR scanned")

    def send_message(self, target):
        try:
            x_arg = '//span[contains(@title,' + target + ')]'
            ct = 0
            while ct != 10:
                try:
                    group_title = self.wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                    group_title.click()
                    break
                except:
                    ct += 1
                    time.sleep(3)
            input_box = self.browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            for ch in self.message:
                if ch == "\n":
                    ActionChains(self.browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    input_box.send_keys(ch)
            input_box.send_keys(Keys.ENTER)
            print("Message sent successfuly")
            time.sleep(1)
        except NoSuchElementException:
            return

    def send_unsaved_contact_message(self):
        try:
            time.sleep(7)
            input_box = self.browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            for ch in self.message:
                if ch == "\n":
                    ActionChains(self.browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    input_box.send_keys(ch)
            input_box.send_keys(Keys.ENTER)
            print("Message sent successfuly")
        except NoSuchElementException:
            print("Failed to send message")
            return


    def send_attachment(self):
        # Attachment Drop Down Menu
        clipButton = self.browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
        clipButton.click()
        time.sleep(1)

        # To send Videos and Images.
        mediaButton = self.browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
        mediaButton.click()
        time.sleep(3)

        hour = datetime.datetime.now().hour

        # After 5am and before 11am scheduled this.
        if(hour >= 5 and hour <= 11):
            image_path = os.getcwd() + "\\Media\\" + 'goodmorning.jpg'
        # After 9pm and before 11pm schedule this
        elif (hour >= 21 and hour <= 23):
            image_path = os.getcwd() + "\\Media\\" + 'goodnight.jpg'
        else:  # At any other time schedule this.
            image_path = os.getcwd() + "\\Media\\" + 'howareyou.jpg'
        # print(image_path)

        autoit.control_focus("Open", "Edit1")
        autoit.control_set_text("Open", "Edit1", (image_path))
        autoit.control_click("Open", "Button1")

        time.sleep(3)
        whatsapp_send_button = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
        whatsapp_send_button.click()

    # Function to send Documents(PDF, Word file, PPT, etc.)


    def send_files(self):
        # Attachment Drop Down Menu
        clipButton = self.browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
        clipButton.click()
        time.sleep(1)

        # To send a Document(PDF, Word file, PPT)
        docButton = self.browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button')
        docButton.click()
        time.sleep(1)

        docPath = os.getcwd() + "\\Documents\\" + self.doc_filename

        autoit.control_focus("Open", "Edit1")
        autoit.control_set_text("Open", "Edit1", (docPath))
        autoit.control_click("Open", "Button1")

        time.sleep(3)
        whatsapp_send_button = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
        whatsapp_send_button.click()


    def sender(self):
        for contact in self.contact:
            send_message(contact)
            print("Message sent to ", contact)
            if(self.choice == "yes"):
                try:
                    send_attachment()
                except:
                    print('Attachment not sent.')
            if(self.docChoice == "yes"):
                try:
                    send_files()
                except:
                    print('Files not sent')
        time.sleep(5)
        if len(self.unsaved_contacts) > 0:
            for contact in self.unsaved_contacts:
                link = "https://wa.me/" + contact
                #driver  = webdriver.Chrome()
                self.browser.get(link)
                time.sleep(1)
                self.browser.find_element_by_xpath('//*[@id="action-button"]').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="content"]/div/div/div/a').click()
                time.sleep(4)
                print("Sending message to", contact)
                send_unsaved_contact_message()
                if(self.choice == "yes"):
                    try:
                        send_attachment()
                    except:
                        print('Attachment not sent.')
                if(self.docChoice == "yes"):
                    try:
                        send_files()
                    except:
                        print('Files not sent')
                time.sleep(7)

    def schedules(self):
        # For GoodMorning Image and Message
        schedule.every().day.at("07:00").do(self.sender)
        # For How are you message
        schedule.every().day.at("13:35").do(self.sender)
        # For GoodNight Image and Message
        schedule.every().day.at("22:00").do(self.sender)

        # Example Schedule for a particular day of week Monday
        schedule.every().monday.at("08:00").do(self.sender)