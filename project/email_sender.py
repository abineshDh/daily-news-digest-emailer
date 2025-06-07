from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

def send_email(subject, body):
    sender = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')
    receiver = os.getenv('EMAIL_TO')
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'html'))
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
    print("Email sent successfully!")
        
