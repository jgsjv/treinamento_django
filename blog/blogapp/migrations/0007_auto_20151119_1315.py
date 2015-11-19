# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_sponsors_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speakers',
            options={'ordering': ['-created'], 'verbose_name': 'Speaker', 'verbose_name_plural': 'Speakers'},
        ),
        migrations.AlterModelOptions(
            name='sponsors',
            options={'ordering': ['-created'], 'verbose_name': 'Sponsor', 'verbose_name_plural': 'Sponsors'},
        ),
        migrations.AddField(
            model_name='speakers',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsors',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 19, 13, 15, 23, 758524, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
