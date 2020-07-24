from django.test import Client, TestCase
from django.urls import reverse

from .models import FamousNames
from .views import add_name, submit_name

class ViewTests(TestCase):

    def test_add_name(self):
        response = self.client.get(reverse('hat:add_name'))
        self.assertEqual(response.status_code, 200)

    def test_submit_name(self):
        testNames = FamousNames.objects.count()
        self.assertEqual(testNames, 0)
        c = Client()
        response = c.post(reverse('hat:submit_name'), {'famous_name': 'Maya Angelou'})
        self.assertEqual(response.status_code, 200)
        testNames = FamousNames.objects.count()
        self.assertEqual(testNames, 1)
        testFamousName = FamousNames.objects.get().name_text
        self.assertEqual(testFamousName, "Maya Angelou")

    def test_submit_blank_name_doesnt_save(self):
        c = Client()
        response = c.post(reverse('hat:submit_name'), {'famous_name': ''})
        testNames = FamousNames.objects.count()
        self.assertEqual(testNames, 0)
