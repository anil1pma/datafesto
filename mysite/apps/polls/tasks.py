# from celery import task
# from .models import User
import datetime
import pytz
from celery.task import PeriodicTask
from datetime import timedelta
from django.core.mail import EmailMessage
from polls.models import SendMessage
import requests
import socket
from django.conf import settings
from django.template import loader, Context
from django.utils import timezone


class ProcessClicksTask(PeriodicTask):
    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        process_clicks()

def process_clicks():
    print '-- celery task process_clicks at  ' + str(timezone.now())
    date_time = timezone.now()
    send_message(date_time)

def send_message(date_time):
    send_message_obj = SendMessage.objects.filter(user_msg_date_time__lte=date_time)
    for obj in send_message_obj:
        id = obj.id
        message = obj.user_message
        mobile_no =  obj.user_mob_no
        mail_id = obj.user_mail_id
        mess_through = obj.user_message_through.split('|')
        try:
            if len(mail_id) > 0 and 'Email' in mess_through:
                subject = 'Your RML message'
                to_user_list = [mail_id]
                mail_html = loader.get_template('user_message.html')
                data = Context({"mail_id": mail_id, "message": message})
                content = mail_html.render(data)
                msg = EmailMessage(subject, content, settings.EMAIL_HOST_USER, to_user_list)
                msg.content_subtype = "html"
                msg.send()
                SendMessage.objects.get(id=id).delete()
        except socket.gaierror:
            pass

        if len(mobile_no) > 0 and 'SMS' in mess_through:
            sms_url = settings.SMS_VENDOR_URL + "?method=SendMessage&msg_type=TEXT&userid=" + settings.SMS_VENDOR_ID + "&auth_scheme=plain&password=" + settings.SMS_VENDOR_PASSWORD + "&v=1.1&format=text&send_to=" + mobile_no + "&msg=" + message
            requests.get(sms_url).text



