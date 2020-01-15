import schedule, time

# To schedule your msgs
def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)