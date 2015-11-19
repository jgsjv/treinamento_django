from django.db import models
from .enum import LEVEL_CHOICES


class EntryQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)

    def startswith_a(self):
        return self.filter(title__istartswith='a')

    def startswith_A(self):
        return self.filter(title__istartswith='A')

    def startswith_any_a(self):
        return self.filter(title__startswith='A')


class SpeakerQuerySet(models.QuerySet):
    pass


class SponsorQuerySet(models.QuerySet):
    pass


class EntryManager(models.Manager):

    def get_queryset(self):
        return EntryQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def startswith_a(self):
        return self.get_queryset().startswith_a()

    def startswith_A(self):
        return self.get_queryset().startswith_A()

    def startswith_any_a(self):
        return self.get_queryset().startswith__any_a()


class SpeakerManager(models.Manager):

    def get_queryset(self):
        return SpeakerQuerySet(self.model, using=self._db)


class SponsorManager(models.Manager):

    def get_queryset(self):
        return SponsorQuerySet(self.model, using=self._db)

    def get_gold(self):
        return self.filter(level='G')

    def get_silver(self):
        return self.filter(level='S')

    def get_bronze(self):
        return self.filter(level='B')

