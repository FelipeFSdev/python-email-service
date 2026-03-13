from pydantic import BaseModel

class IEmailSenderSchema(BaseModel):
    to: str
    subject: str 
    body: str 
    