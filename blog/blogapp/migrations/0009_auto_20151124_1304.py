# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20151119_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsors',
            options={'ordering': ['level'], 'verbose_name': 'Sponsor', 'verbose_name_plural': 'Sponsors'},
        ),
        migrations.AlterField(
            model_name='sponsors',
            name='level',
            field=models.IntegerField(default=3, choices=[(1, b'GOLD'), (2, b'SILVER'), (3, b'BRONZE')]),
        ),
    ]
