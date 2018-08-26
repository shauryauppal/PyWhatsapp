# PyWhatsapp
##  Python Automation using Selenium &amp; Scheduling of messages and media

## Objective:
 Pywhatsapp is used to Automate Whatsapp through Whatsapp web. We can add number of contacts whom we want to send messages or Media attachments ( like Video or Images). Selenium, Autoit and Schedule have been used one from Automation and other for Scheduling messages.

------------------

## Use Case:
 We can schedule Good Morning or Good night messages with a nice Picture at a particular time to our loved ones. We can set reminders. Suppose at 12 o'clock you want to wish your friend happy birthday so schedule your messages and sleep peacefully.

---------------------
## Install

>$ pip install -r requirements.txt

OR

>$ pip install selenium

>$ pip install schedule

>$ pip install PyAutoIt

_________________

### Platform: Windows
ChromeDriver used if this versions becomes outdated or gives problem download the latest version from <a href = "http://chromedriver.chromium.org/downloads"> Download Link </a>

------------------
### For Sending Attachments you need to Install AutoIt (Optional if you only what to send messages):

You may install from the links given below or Install from the folder named "Install AutoIt for Sending Attachments" in the repository.

<a href = "https://www.autoitscript.com/site/autoit/downloads/">Official Website Download Webpage</a>

<a href = "https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.exe"> Installation Link of AutoIt.exe</a>

<a href = "https://www.autoitscript.com/cgi-bin/getfile.pl?../autoit3/scite/download/SciTE4AutoIt3.exe"> AutoitScript Editor (optional to install) </a>

Installation is pretty Simple no changes in setting are required keep everything default. Few clicks on Next and you are done.

------------------

## Code:
### input_contacts()

In this functions Contacts list can be hardcoded or you can give input accordingly.(Make changes in Contact array according to you)

>Enter number of Contacts to add-> 2

>Enter contact names-> Rahul

>Enter contact name-> Shauryauppal

### input_message()
In this function we take input of message to send to all the Contacts list from user.

Example:
> Enter the msg to send-> Good morning

### Enter choice whether to send attachments or not.
> Would you like to send attachment(yes/no): yes
Answer the input with yes or no.

### send_attachments()
NOTE: Add Photos & Videos in the Media Folder.

image_path = os.getcwd() +"\\Media\\" + 'goodmorning.jpg'

Example path to send goodmorning image to your listed Contacts.

* "hour" variable is used to check current Hour on the clock and according image is sent to the Contact.
* If time is after 5am and before 11am schedule goodmorning.jpg image.
* If time is after 9pm schedule goodnight image.
* If time is anyother send howareyou image.

You can set your own photos at a particular time feel free to do that.

### send_files()
NOTE: Add the document in the documents folder.
> Would you file to send a Document file(yes/no): yes

> Enter the Document file name you want to send: opportunity

* If the document file names are same then write the document name with extension like opportunity.pdf or opportunity.txt


### Schedule messages and Attachments
schedule.every().Monday.at("06:00").do(sender)

schedule.every().Tuesday.at("07:00").do(sender)

schedule.every().Friday.at("07:30").do(sender)

schedule.every().day.at("08:30").do(sender)

* You make change these schedule days and time according to you.

------------
### Demo of Working (GIF)
<img src="https://raw.githubusercontent.com/shauryauppal/PyWhatsapp/master/Media/Demo.gif" height=400 width=400/>

------------

## Contributions
<a href="https://github.com/shauryauppal/PyWhatsapp/issues"> Issues </a> and <a href ="https://github.com/shauryauppal/PyWhatsapp/pulls"> Pull requests </a> are most welcome.

-------------------
## License
License
Code and documentation are available according to the Apache License (see <a href="https://github.com/shauryauppal/PyWhatsapp/blob/master/LICENSE">LICENSE</a>).

---------------------

### Author:
#### Shaurya Uppal
shauryauppal00111@gmail.com

Feel free to mail me for any queries.

##### Don't forget to give me Credits in case it helps you.
