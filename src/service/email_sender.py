from src.adapters.email_sender_gateway import IEmailSenderGateway

class EmailSenderService():
    def __init__(self, email_gateway: IEmailSenderGateway):
        self.email_gateway = email_gateway
    
    def send_email(self,to: str, subject: str, body: str):
        self.email_gateway.send_email(
            to,
            subject,
            body
        )
        