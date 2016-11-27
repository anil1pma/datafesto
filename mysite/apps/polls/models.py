from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_mob_no  = models.CharField(max_length=20)
    user_mail_id = models.EmailField(max_length=50)
    user_message = models.CharField(max_length=1000, blank=True)
