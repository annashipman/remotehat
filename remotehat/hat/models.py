from django.db import models


class FamousNames(models.Model):
    name_text = models.CharField(max_length=200)
    round_number = models.IntegerField(default=1)

class Rounds(models.Model):
    current_round = models.IntegerField(default=1)
