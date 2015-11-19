# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20151119_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speakers',
            options={'verbose_name': 'Speaker', 'verbose_name_plural': 'Speakers'},
        ),
        migrations.AlterModelOptions(
            name='sponsors',
            options={'verbose_name': 'Sponsor', 'verbose_name_plural': 'Sponsors'},
        ),
        migrations.RemoveField(
            model_name='speakers',
            name='created',
        ),
        migrations.RemoveField(
            model_name='sponsors',
            name='created',
        ),
    ]
