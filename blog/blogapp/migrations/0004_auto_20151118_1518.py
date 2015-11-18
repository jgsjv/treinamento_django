# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20151118_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speakers',
            options={'verbose_name': 'Speaker', 'verbose_name_plural': 'Speakers'},
        ),
        migrations.AddField(
            model_name='speakers',
            name='picture',
            field=models.ImageField(default=datetime.datetime(2015, 11, 18, 15, 18, 9, 718055, tzinfo=utc), upload_to=b'speakers'),
            preserve_default=False,
        ),
    ]
