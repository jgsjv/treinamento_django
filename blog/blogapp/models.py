from django.db import models
from django_markdown.models import MarkdownField
from .managers import EntryManager, SpeakerManager, SponsorManager
from .enum import LEVEL_CHOICES
from .enum import BRONZE


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = EntryManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
        ordering = ["-created"]


class Speakers(models.Model):
    name = models.CharField(max_length=200)
    ocupation = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='speakers')
    objects = SpeakerManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"

    def go(self):
        return self.name.lower()


class Sponsors(models.Model):
    brand = models.CharField(max_length=200)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=BRONZE)
    picture = models.ImageField(upload_to='sponsors')
    objects = SponsorManager()

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
        ordering = ['level']
