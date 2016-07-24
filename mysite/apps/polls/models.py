from django.db import models
from datetime import datetime
from datetime import date


class SendMessage(models.Model):
    user_mob_no  = models.CharField(max_length=20)
    user_message = models.CharField(max_length=250, blank=True)
    user_mail_id = models.EmailField(max_length=50)
    user_message_through = models.CharField(max_length=20)
    user_msg_date_time = models.DateTimeField(blank=True, null=True)



