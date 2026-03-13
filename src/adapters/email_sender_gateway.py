from abc import ABC, abstractmethod

class IEmailSenderGateway(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> None:
        """
        Define contrato para envio de emails.
        """
        pass
