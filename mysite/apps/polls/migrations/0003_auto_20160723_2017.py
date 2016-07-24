# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160723_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmessage',
            name='user_message',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]
