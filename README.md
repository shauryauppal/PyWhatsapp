# PyWhatsapp
##  Python Automation using selenium &amp; Scheduling of messages

## Objective:
 Pywhatsapp is used to Automate Whatsapp through Whatsapp web. We can add number of contacts whom we want to send messages. Selenium and Schedule have been used one from Automation and other for Scheduling messages.

------------------

### Use Case:
 We can schedule Good Morning or Good night messages at a particular time for are loved ones. We can set reminders. Suppose at 12 o'clock you want to wish your friend happy birthday so schedule your messages sleep nicely.

---------------------
## Install

>$ pip install -r requirements.txt

OR

>$ pip install selenium

>$ pip install schedule

------------------

## Code:
#### input_contacts()

In this functions Contacts list can be hardcoded or you can give input accordingly.(Make changes in Contact array according to you)

>Enter number of Contacts to add-> 2

>Enter contact names-> "Rahul"

>Enter contact name-> "Shauryauppal"

#### input_message()
In this function we take input of message to send to all the Contacts list from user.

Example:
> Enter the msg to send-> Good morning

#### Schedule messages
schedule.every().Monday.at("06:00").do(sender)

schedule.every().Tuesday.at("07:00").do(sender)

schedule.every().Friday.at("07:30").do(sender)

schedule.every().day.at("08:30").do(sender)

* You make change these schedule days and time according to you.


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
