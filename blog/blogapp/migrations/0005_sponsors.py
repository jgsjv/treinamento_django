# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20151118_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=200)),
                ('level', models.CharField(default=b'B', max_length=1, choices=[(b'G', b'GOLD'), (b'S', b'SILVER'), (b'B', b'BRONZE')])),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
            },
        ),
    ]
