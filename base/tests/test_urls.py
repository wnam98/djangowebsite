from django.test import SimpleTestCase
from django.urls import reverse, resolve;

class TestUrls(SimpleTestCase):
    
    def test_url(self):
        url = reverse(' ');
        print(resolve(url))
