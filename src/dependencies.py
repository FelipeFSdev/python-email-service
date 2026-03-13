from fastapi import Depends
from typing import Annotated

from src.service.email_sender import EmailSenderService
from src.infra.smtp_server import MailMugEmailSender
from src.adapters.email_sender_gateway import IEmailSenderGateway

def get_email_gateway() -> IEmailSenderGateway:
    return MailMugEmailSender()

EmailGatewayDep = Annotated[IEmailSenderGateway, Depends(get_email_gateway)]

def get_email_service(gateway: EmailGatewayDep) -> EmailSenderService:
    return EmailSenderService(gateway)

EmailServiceDep = Annotated[EmailSenderService, Depends(get_email_service)]