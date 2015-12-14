# -*- coding: utf-8 -*-

from django.test import TestCase
from blogapp.forms import EventoForm
from blogapp.models import Entry
from blogapp.models import Sponsors
from blogapp.models import Speakers
from .enum import LEVEL_CHOICES
from .enum import GOLD, SILVER, BRONZE
from django.core.urlresolvers import reverse
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

lista_de_urls = {
        'home': '/home',
        'patrocinadores': '/sponsor',
        'palestrantes': '/speaker',
        'noticias': '/news',
        'evento': '/event',
        'agradecimento': '/thanks',
        'publicacao': '(?P<pk>[\d]+)',
    }


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

    fixtures = ['blogapp']

    def test_index(self):
        resp = self.client.get('/news')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('news' in resp.context)

# Voltar para esse aqui.


class PublicacoesDetalhesTestCase(TestCase):

    def test_index(self):
        for chave, url in lista_de_urls.iteritems():
            url = reverse('publicacao', args=(publicacao.pk,))
        url_desejada = 'publicacoes/{0}/detalhes'.format(self.entries)
        self.assertEqual(url, url_desejada)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class BlogIndexTestCase(TestCase):

    fixtures = ['blogapp']

    def test_index(self):
        for chave, url in lista_de_urls.iteritems():
            url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class SpeakerIndexTestCase(TestCase):

    def test_index(self):
        for chave, url in lista_de_urls.iteritems():
            url = reverse('palestrantes')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('speakers' in resp.context)


class SponsorIndexTestCase(TestCase):

    def test_index(self):
        for chave, url in lista_de_urls.iteritems():
            url = reverse('patrocinadores')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('sponsors' in resp.context)


class EventoViewTestCase(TestCase):

    def test_index(self):
        for chave, url in lista_de_urls.iteritems():
            url = reverse('evento')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class ThanksViewTestCase(TestCase):

    def test_index(self):
        for chave, url in lista_de_urls.iteritems():
            url = reverse('agradecimento')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

# Testes de managers.

# Testes de forms.


# class EventoFormTestCase(TestCase):

    # def test_good_contact(self):
    #     post = EventoForm.object.get(pk=1)
    #    resp = self.client.post('evento', {'subject': Testes, 'message': Comentario ou sugestao, 'sender': jgsjv@cin.ufpe.br})
    #    self.assertEqual(resp.satus_code, 200)

