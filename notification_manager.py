import os
import smtplib

from lxml.html.builder import SELECT
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.smtp_address = os.getenv("SMTP_ADDRESS")
        self.email = os.getenv("EMAIL")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.senders_number = os.getenv("SENDERS_NUMBER")
        self.receivers_number = os.getenv("RECEIVERS_NUMBER")


        self.client = Client(os.getenv("API_KEY_MSG"), os.getenv("AUTH_TOKEN_MSG"))
        self.connection = smtplib.SMTP("smtp.gmail.com")


    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=self.senders_number,
            body=message_body,
            to=self.receivers_number
        )
        # Prints if successfully sent.
        print(message.sid)

    # def send_whatsapp(self, message_body):
    #     message = self.client.messages.create(
    #         from_="+14633005387",
    #         body=message_body,
    #         to="+917387906926"
    #     )
    #     print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )

        print("mail send")