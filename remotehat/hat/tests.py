from django.test import TestCase
from django.urls import reverse

from .views import add_name, submit_name

class ViewTests(TestCase):

    def test_add_name(self):
        response = self.client.get(reverse('hat:add_name'))
        self.assertEqual(response.status_code, 200)

    def test_submit_name(self):
        response = self.client.get(reverse('hat:submit_name'))
        self.assertEqual(response.status_code, 200)

