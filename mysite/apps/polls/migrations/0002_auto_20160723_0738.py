# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendmessage',
            old_name='user_message_sending_time',
            new_name='user_msg_date_time',
        ),
        migrations.AlterField(
            model_name='sendmessage',
            name='user_mail_id',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='sendmessage',
            name='user_message_through',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sendmessage',
            name='user_mob_no',
            field=models.CharField(max_length=20),
        ),
    ]
