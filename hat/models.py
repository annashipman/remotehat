from django.db import models


class FamousNames(models.Model):
    name_text = models.CharField(max_length=200)
    round_number = models.IntegerField(default=0)
