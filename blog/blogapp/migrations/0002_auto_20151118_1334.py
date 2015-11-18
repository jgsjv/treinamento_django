# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
