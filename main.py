import schedule
from time import sleep,time

time1 = time()
def job():
    #put code to be run hourly in here
    print("This code is working...")
    print(time1-time())


schedule.every(1.5).hours.do(job)

while True:
    schedule.run_pending()
    sleep(1)
