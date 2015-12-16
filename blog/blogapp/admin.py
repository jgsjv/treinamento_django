# -*- coding: utf-8 -*-

from .models import Entry
from .models import Speakers
from .models import Sponsors
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin


@admin.register(Entry)
class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "publish", )
    list_filter = ['publish']


@admin.register(Speakers)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "picture")
    prepolated_fileds = {"name": ("name",)}


@admin.register(Sponsors)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("brand", "level",)
    list_filter = ['level', ]
