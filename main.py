import schedule
from time import sleep


def job():
    #put code to be run hourly in here
    print("This code is working...")


schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    sleep(1)
