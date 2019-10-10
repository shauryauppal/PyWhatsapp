import schedule






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

    # Append more contact as input to send messages
    input_contacts()
    # Enter the message you want to send
    input_message()

    # If you want to schedule messages for
    # a particular timing choose yes
    # If no choosed instant message would be sent
    isSchedule = input('Do you want to schedule your Message(yes/no):')
    if(isSchedule == "yes"):
        jobtime = input('input time in 24 hour (HH:MM) format - ')

    # Send Attachment Media only Images/Video
    choice = input("Would you like to send attachment(yes/no): ")

    docChoice = input("Would you file to send a Document file(yes/no): ")
    if(docChoice == "yes"):
        # Note the document file should be present in the Document Folder
        doc_filename = input("Enter the Document file name you want to send: ")

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login()

    # Send message to all Contact List
    # This sender is just for testing purpose to check script working or not.
    # Scheduling works below.
    # sender()
    # Uncomment line 236 is case you want to test the program

    if(isSchedule == "yes"):
        schedule.every().day.at(jobtime).do(sender)
    else:
        sender()

    # First time message sending Task Complete
    print("Task Completed")

    # Messages are scheduled to send
    # Default schedule to send attachment and greet the personal
    # For GoodMorning, GoodNight and howareyou wishes
    # Comment in case you don't want to send wishes or schedule
    scheduler()

    # browser.quit()
