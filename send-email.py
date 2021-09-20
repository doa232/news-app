import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from newspaper_project.settings import EMAIL_HOST_PASSWORD

message = Mail(from_email='sherleyf2@jnswritesy.com',
               to_emails='doadoadaodao6@gmail.com',
               subject='Sending Test',
               plain_text_content=' Hello world',
               html_content='<strong>Hello World</strong>')
try:
    sg = SendGridAPIClient(EMAIL_HOST_PASSWORD)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
