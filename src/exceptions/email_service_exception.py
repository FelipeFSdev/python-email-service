from smtplib import SMTPException

class EmailServiceException(SMTPException):
    def __init__(self, message: str, strerror: str | None):
        super().__init__(message, strerror)
        
