from email_service import EmailService
from sms_service import SMSService

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()   # this two objects that depend on low level module
        self.sms_service = SMSService()       # not flexibility

    def notifyByEmail(self, message):
        self.email_service.send_email(message)
    
    def notifyBySMS(self, message):
        self.sms_service.send_sms(message)
    

ns = NotificationService()
ns.notifyByEmail("Good")
ns.notifyBySMS("Hey")