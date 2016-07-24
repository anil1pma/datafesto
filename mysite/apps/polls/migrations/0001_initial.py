# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_mob_no', models.CharField(default=b'', max_length=20, blank=True)),
                ('user_message', models.CharField(max_length=20, blank=True)),
                ('user_mail_id', models.EmailField(unique=True, max_length=254)),
                ('user_message_through', models.CharField(default=b'', max_length=20, blank=True)),
                ('user_message_sending_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
