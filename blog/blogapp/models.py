from django.db import models
from django_markdown.models import MarkdownField


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class SpeakerQuerySet(models.QuerySet):
    def __str__(self):
        return self


class SponsorQuerySet(models.QuerySet):
    def __str__(self):
        return self


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]


class Speakers(models.Model):
    name = models.CharField(max_length=200)
    ocupation = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='speakers')
    member = SpeakerQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"


class Sponsors(models.Model):
    brand = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    GOLD = 'G'
    SILVER = 'S'
    BRONZE = 'B'
    LEVEL_CHOICES = (('G', 'GOLD'),
                     ('S', 'SILVER'),
                     ('B', 'BRONZE'))
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES,
                             default=BRONZE)
    picture = models.ImageField(upload_to='sponsors')
    objects = SponsorQuerySet.as_manager()

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
        ordering = ["-created"]
