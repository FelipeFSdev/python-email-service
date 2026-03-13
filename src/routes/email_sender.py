from fastapi import APIRouter, HTTPException

from src.exceptions.email_service_exception import EmailServiceException
from src.dependencies import EmailServiceDep
from src.schema.email_sender import IEmailSenderSchema


router = APIRouter()

@router.post("/api/email")
def sendEmail(email_service: EmailServiceDep, request: IEmailSenderSchema):
    try:
        email_service.send_email(
            request.to,
            request.subject,
            request.body
            )
        return  {"message":"Email send succesfully."}
    except EmailServiceException as ex:
        print(ex)
        raise HTTPException(
            status_code=500,
            detail="Failure while sending email"
            )
    except Exception as ex:
        print(ex)
        raise HTTPException(
            status_code=500,
            detail="Unexpected error."
        )
    