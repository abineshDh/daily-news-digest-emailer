# 📰 Daily News Mailer

This is a simple Python automation project that uses [NewsAPI](https://newsapi.org/) to fetch the latest top news headlines and sends them to your email using SMTP. The project runs at a defined interval using a scheduler, delivering a clean news summary straight to your inbox.

---

## 🚀 Features

- ✅ Fetch top news headlines using **NewsAPI**
- ✅ Send daily summary via **Gmail SMTP**
- ✅ Scheduled delivery using **Python schedule**
- ✅ `.env` support for secure credentials
- ✅ Easily customizable for keywords, country, or news source

---

## 🔧 Tech Stack

- **Python 3**
- [`requests`](https://pypi.org/project/requests/) – for fetching news from NewsAPI  
- [`smtplib`](https://docs.python.org/3/library/smtplib.html) – for sending emails via Gmail SMTP  
- [`email.mime`](https://docs.python.org/3/library/email.mime.html) – for formatting email content  
- [`schedule`](https://pypi.org/project/schedule/) – for running the job daily  
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) – for managing secrets from `.env`

---

## 🛠 How It Works
- news_fetcher.py: Connects to NewsAPI and fetches top 5 headlines.
- email_sender.py: Sends the formatted news summary to your inbox.
- scheduler.py: Schedules the email job using schedule.
- main.py: Starts the whole process and sends email at a defined time.

---

## 📦 Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/daily-news-mailer.git
cd daily-news-mailer
main.py
