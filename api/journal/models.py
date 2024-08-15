from django.db import models
from datetime import date

CHECKLIST = [
    "exercised",
    "learned",
    "socialized",
    "meditated",
    "alcohol",
    "cleaned",
    "ate_healthy",
    "hydrated",
]


KEYWORDS = [
    "acceptable",
    "accomplished",
    "affectionate",
    "afraid",
    "alive",
    "alone",
    "angry",
    "annoyed",
    "anxious",
    "appreciated",
    "assertive",
    "attractive",
    "bored",
    "cared for",
    "caring",
    "confident",
    "conflicted",
    "confused",
    "connected",
    "courageous",
    "damaged",
    "depressed",
    "determined",
    "disappointed",
    "distracted",
    "drained",
    "elated",
    "embarrassed",
    "fascinated",
    "focused",
    "good",
    "guilty",
    "happy",
    "helpless",
    "hurt",
    "hurtful",
    "imaginative",
    "inadequate",
    "indecisive",
    "indifferent",
    "inspired",
    "intelligent",
    "interested",
    "invisible",
    "lazy",
    "logical",
    "lost",
    "loved",
    "loving",
    "negative",
    "nurturing",
    "observant",
    "okay",
    "open",
    "overwhelmed",
    "passionate",
    "playful",
    "positive",
    "productive",
    "rebellious",
    "relaxed",
    "sad",
    "satisfied",
    "self-conscious",
    "selfless",
    "shocked",
    "sick",
    "smart",
    "spirited",
    "stressed",
    "strong",
    "thankful",
    "tired",
    "uncomfortable",
    "uneventful",
    "victimized",
    "vulnerable",
    "worried",
]


class JournalEntryKeyword(models.Model):
    name = models.TextField()
    color = models.TextField()


class JournalEntryMeter(models.Model):
    keyword = models.ForeignKey(JournalEntryKeyword)
    emoji = models.TextField(default="")
    level = models.PositiveIntegerField(default=0)


class JournalEntryChecklist(models.Model):
    name = models.TextField()
    checked = models.BooleanField(default=False)


class JournalEntry(models.Model):
    date = models.DateField(default=date.today)
    summary = models.TextField()
    thankful_note = models.TextField()
    struggle_note = models.TextField()
    hours_slept = models.PositiveIntegerField()
    meters = models.ManyToManyField(JournalEntryMeter)
    keywords = models.ManyToManyField(JournalEntryKeyword)
    checklist = models.OneToOneField(JournalEntryChecklist)

    def save(self):
        instance = super().save()
