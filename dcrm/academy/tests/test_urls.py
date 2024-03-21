from django.test import TestCase
from django.urls import reverse, resolve
from academy.views import home


class TestUrls(TestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url), home)
