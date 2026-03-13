import os
from dotenv import load_dotenv
from smtplib import SMTP, SMTPException
from contextlib import contextmanager
from email.message import EmailMessage

from src.adapters.email_sender_gateway import IEmailSenderGateway
from src.exceptions.email_service_exception import EmailServiceException

load_dotenv()

class MailMugEmailSender(IEmailSenderGateway):
    def __init__(self):
        self.host = os.getenv("SMTP_HOST","")
        self.port = int(os.getenv("SMTP_PORT", "2525"))
        self.user = os.getenv("SMTP_USER","")
        self.password = os.getenv("SMTP_PASS","")

    @contextmanager
    def __create_smtpserver(self):
        with SMTP(self.host, self.port) as smtp:
            smtp.login(self.user, self.password)
            yield smtp
        

    def send_email(self, to: str, subject: str, body: str):
        message = EmailMessage()
        message.set_content(body)
        message["subject"] = subject
        message["to"] = to
        message["from"] = os.getenv("MY_TEST_EMAIL")
        try:
            with self.__create_smtpserver() as server:
                server.send_message(message)

            return None 
        
        except SMTPException as ex:
            raise EmailServiceException("Failure while sending email", str(ex))