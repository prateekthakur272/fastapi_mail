from dotenv import dotenv_values
from ssl import create_default_context
from email.mime.text import MIMEText
from email.message import EmailMessage
from smtplib import SMTP_SSL


env_values = dotenv_values('.env')

# add the following to .env file
# HOST = ''
# USERNAME = ''
# PASSWORD = ''
# PORT = ''

HOST = env_values['HOST']
USERNAME = env_values['USERNAME']
PASSWORD = env_values['PASSWORD']
PORT = env_values['PORT']

async def send_mail(subject:str, body:str, to:str): 
    # create email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = USERNAME
    msg['To'] = to
    msg.set_content(body)
    # send email
    with SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(USERNAME, PASSWORD)
        smtp.send_message(msg)