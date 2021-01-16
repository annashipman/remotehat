# Generated by Django 3.1.3 on 2020-11-20 16:19

from django.db import migrations


class Migration(migrations.Migration):

    def set_round_to_1(apps, schema_editor):
        # We can't import the Rounds model directly as it may be a newer
        # version than this migration expects. We use the historical version.
        Rounds = apps.get_model("hat", "Rounds")
        # there is no current round
        # i need to set it
        initial_round = Rounds(current_round = 1)
        initial_round.save()

    dependencies = [
        ('hat', '0002_auto_20201120_1118'),
    ]

    operations = [
        migrations.RunPython(set_round_to_1),
    ]