from django.db import models
from datetime import date


class EntryMeter(models.Model):
    name = models.TextField()
    emoji = models.TextField()
    level = models.PositiveIntegerField(default=0)


class EntryKeyword(models.Model):
    keyword = models.TextField()


class EntryChecklist(models.Model):
    name = models.TextField()
    done = models.BooleanField(default=False)

    exercised = models.BooleanField(default=False)
    learned = models.BooleanField(default=False)
    socialized = models.BooleanField(default=False)
    meditated = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    cleaned = models.BooleanField(default=False)
    ate_healthy = models.BooleanField(default=False)
    hydrated = models.BooleanField(default=False)


class JournalEntry(models.Model):
    date = models.DateField(default=date.today)
    summary = models.TextField()
    thankful_note = models.TextField()
    struggle_note = models.TextField()
    hours_slept = models.PositiveIntegerField()
    meters = models.ManyToManyField(EntryMeter)
    keywords = models.ManyToManyField(EntryKeyword)
    checklist = models.ForeignKey(EntryChecklist)
