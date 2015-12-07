# -*- coding: utf-8 -*-

from django.test import TestCase
from blogapp.models import Entry


class EntryTestCase(TestCase):

    def setUp(self):
        self.entry = Entry.objects.create(
            title='titulo x',
            publish=True,
        )

    def test_published_entries(self):
        self.assertEqual(self.entry.title, 'titulo x')
        self.assertTrue(self.entry.publish)
        import ipdb; ipdb.set_trace()
        self.assertEquals(Entry.objects.published(),
                          Entry.objects.filter(publish=True))


