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

    def test_retrieve_random_name_increments_successful_guess(self):
        rainer_maria_rilke = FamousNames(name_text = "Rainer Maria Rilke")
        rainer_maria_rilke.save()
        famousNameRound = FamousNames.objects.get().round_number
        self.assertEqual(famousNameRound, 1)
        c = Client()
        response = c.post(reverse('hat:retrieve_random_name'), {'famous_name': 'Rainer Maria Rilke'})
        famousNameRound = FamousNames.objects.get().round_number
        self.assertEqual(famousNameRound, 2)

    def test_retrieve_random_name_no_names_left(self):
        round = 1
        self.assertFalse(FamousNames.objects.filter(round_number=round))
        mary_seacole = FamousNames(name_text = "Mary Seacole")
        mary_seacole.save()
        c = Client()
        response = c.post(reverse('hat:retrieve_random_name'), {'famous_name': 'Mary Seacole'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue("No names left in hat! End of round 1" in response.content.decode("utf-8"))


    def test_round_automatically_increments(self):
        mary_seacole = FamousNames(name_text = "Mary Seacole")
        mary_seacole.save()
        rainer_maria_rilke = FamousNames(name_text = "Rainer Maria Rilke")
        rainer_maria_rilke.save()
        self.assertEqual(FamousNames.objects.filter(round_number=1).count(), 2)
        c = Client()
        response = c.post(reverse('hat:retrieve_random_name'), {'famous_name': 'Mary Seacole'})
        response = c.post(reverse('hat:retrieve_random_name'), {'famous_name': 'Rainer Maria Rilke'})
        self.assertTrue("No names left in hat! End of round 1" in response.content.decode("utf-8"))
        self.assertEqual(FamousNames.objects.filter(round_number=1).count(), 0)
        self.assertEqual(FamousNames.objects.filter(round_number=2).count(), 2)

        ## Now testing it can retrieve from round 2 without manual intervention
        response = c.post(reverse('hat:retrieve_random_name'), {'famous_name': 'Mary Seacole'})
        response = c.post(reverse('hat:retrieve_random_name'), {'famous_name': 'Rainer Maria Rilke'})
        self.assertEqual(FamousNames.objects.filter(round_number=2).count(), 0)
