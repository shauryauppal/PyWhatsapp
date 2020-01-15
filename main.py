import schedule

from pywhatsapp.scheduler import scheduler
from pywhatsapp.client import client


if __name__ == "__main__":
    _client = client()
    _client.schedules()
    print("Web Page Open")

    # Append more contact as input to send messages
    _client.input_contacts()
    # Enter the message you want to send
    _client.input_message()

    # If you want to schedule messages for
    # a particular timing choose yes
    # If no choosed instant message would be sent
    isSchedule = input('Do you want to schedule your Message(yes/no):')
    if(isSchedule == "yes"):
        jobtime = input('input time in 24 hour (HH:MM) format - ')

    # Send Attachment Media only Images/Video
    _client.choice = input("Would you like to send attachment(yes/no): ")

    _client.docChoice = input("Would you file to send a Document file(yes/no): ")
    if(_client.docChoice == "yes"):
        # Note the document file should be present in the Document Folder
        doc_filename = input("Enter the Document file name you want to send: ")

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    _client.whatsapp_login()

    # Send message to all Contact List
    # This sender is just for testing purpose to check script working or not.
    # Scheduling works below.
    # sender()
    # Uncomment line 236 is case you want to test the program

    if(isSchedule == "yes"):
        schedule.every().day.at(jobtime).do(_client.sender)
    else:
        _client.sender()

    # First time message sending Task Complete
    print("Task Completed")

    # Messages are scheduled to send
    # Default schedule to send attachment and greet the personal
    # For GoodMorning, GoodNight and howareyou wishes
    # Comment in case you don't want to send wishes or schedule
    scheduler()

    # browser.quit()



