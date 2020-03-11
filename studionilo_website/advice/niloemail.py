from django.core.mail import send_mail
from django.conf import settings
from .models import PaymentIntent
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class NiloEmail:
    def __init__(self, payIntent):
        self.payIntent = payIntent
    
    def send(self):
        email_from = settings.EMAIL_HOST_USER
        html_message = self.__message()
        plain_message = strip_tags(html_message)
        send_mail( self.__subject(), plain_message, email_from, self.__recipient_list(), html_message=html_message)
    
    def __subject(self):
        if(self.payIntent.plan == PaymentIntent.VIDEOREPORT):
            return 'Fantastico! Riceverai un video-report sulla tua presenza digitale - studionilo.it'
        elif(self.payIntent.plan == PaymentIntent.VIDEOCOLLOQUIO):
            return 'Fantastico! Riceverai un video-colloquio sulla tua presenza digitale - studionilo.it'
        else:
            return 'Fantastico! Ti ricontatteremo presto per parlarti nel nostro servizio di social media managing - studionilo.it'            

    def __message(self):
        if(self.payIntent.plan == PaymentIntent.VIDEOREPORT):
            return render_to_string('advice/email_video_report.html')
        elif(self.payIntent.plan == PaymentIntent.VIDEOCOLLOQUIO):
            return render_to_string('advice/email_video_colloquio.html')
        else:
            return render_to_string('advice/email_media_managing.html')

    def __recipient_list(self):
        return [self.payIntent.email, ]