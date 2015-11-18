# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20151118_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('ocupation', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Rules',
        ),
    ]
