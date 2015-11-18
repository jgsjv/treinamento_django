from django.contrib import admin
from . import models
from .models import Speakers, Sponsors
from django_markdown.admin import MarkdownModelAdmin


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title")}


admin.site.register(models.Entry)


class SpeakerAdmin():
    list_display = ("name", "subject", "picture")
    prepolated_fileds = {"name": ("name")}


admin.site.register(Speakers)


class SponsorAdmin():
    list_display = ("brand", "level",)

admin.site.register(Sponsors)
