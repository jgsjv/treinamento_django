# -*- coding: utf-8 -*-

from django.test import TestCase
from blogapp.forms import EventoForm
from blogapp.models import Entry
from blogapp.models import Sponsors
from blogapp.models import Speakers
from .enum import LEVEL_CHOICES
from .enum import BRONZE


class EntryTestCase(TestCase):

    def setUp(self):
        self.entry = Entry.objects.create(
            title='titulo x',
            publish=True,
        )

    def test_published_entries(self):
        self.assertEqual(self.entry.title, 'titulo x')
        self.assertTrue(self.entry.publish)
        # import ipdb; ipdb.set_trace()
        # self.assertEqual(Entry.objects.published())


class SpeakerTestCase(TestCase):

    def setUp(self):
        self.speaker = Speakers.objects.create(
            name='palestrante y',
            ocupation='motivador',
            subject='titulo longo de palestra',
            # picture=não sei o que por aqui por enquanto
            )

    def test_speaker_creation(self):
        self.assertEqual(self.speaker.name, 'palestrante y')
        self.assertEqual(self.speaker.ocupation, 'motivador')
        self.assertEqual(self.speaker.subject, 'titulo longo de palestra')


class SponsorTestCase(TestCase):

    def setUp(self):
        self.sponsor = Sponsors.objects.create(
            brand='marca z',
            level=BRONZE
            # picture=não sei o que por aqui por enquanto
            )

    def test_sponsor_creation(self):
        self.assertEqual(self.sponsor.brand, 'marca z')
        self.assertEqual(self.sponsor.level, BRONZE)
