# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_sponsors'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsors',
            name='picture',
            field=models.ImageField(default=datetime.datetime(2015, 11, 18, 16, 16, 34, 942326, tzinfo=utc), upload_to=b'sponsors'),
            preserve_default=False,
        ),
    ]
