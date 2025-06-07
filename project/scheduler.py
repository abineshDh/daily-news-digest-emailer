import schedule
import datetime
import time
from news_fetcher import get_headlines
from email_sender import send_email

def job():
    headlines = get_headlines()
    body = "<br>".join([line.replace("\n", "<hr>") for line in headlines])
    send_email(f"Daily News Digest - (python_automation)", body)
    
def run():
    now = datetime.datetime.now()
    run_time = (now + datetime.timedelta(minutes=1)).strftime("%H:%M")
    schedule.every().day.at(run_time).do(job)
    print(f'Scheduled for {run_time}')
    while True:
        schedule.run_pending()
        time.sleep(60)