import schedule
import time

def dispatch(job):
    job()

def working():
    print("I'm working...")

if __name__ == '__main__':
    schedule.every(5).seconds.do(dispatch, working)

    while True:
        schedule.run_pending()
        time.sleep(1)
