# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160723_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmessage',
            name='user_mail_id',
            field=models.EmailField(max_length=50),
        ),
    ]
