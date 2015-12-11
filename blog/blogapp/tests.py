# -*- coding: utf-8 -*-

from django.test import TestCase
from blogapp.forms import EventoForm
from blogapp.models import Entry
from blogapp.models import Sponsors
from blogapp.models import Speakers
from .enum import LEVEL_CHOICES
from .enum import GOLD, SILVER, BRONZE

# Testes de criacao de models.


class EntryTestCase(TestCase):

    fixtures = ['blogapp']

    def test_published_entries(self):
        s = Entry.objects.get(pk=1)
        self.assertEquals(s.title, 'Bicicletas compartilhadas do Projeto Bike PE tem horario estendido aos domingos e feriados')
        self.assertTrue(s.publish)


class SpeakerTestCase(TestCase):

    fixtures = ['blogapp']

    def test_speaker_creation(self):
        t = Speakers.objects.get(pk=1)
        self.assertEqual(t.name, 'Dennis McField')
        self.assertEqual(t.ocupation, 'Enterteiner')
        self.assertEqual(t.subject, 'The show must go on')


class SponsorTestCase(TestCase):

    fixtures = ['blogapp']

    def test_sponsor_creation(self):
        u = Sponsors.objects.get(pk=1)
        self.assertEqual(u.brand, 'Colgate')
        self.assertEqual(u.level, GOLD)


# Testes de views.

class NewsIndexTestCase(TestCase):

    def test_index(self):
        resp = self.client.get('/news')
        self.assertEqual(resp.status_code, 200)



















# Testes de managers.

# Testes de forms.

