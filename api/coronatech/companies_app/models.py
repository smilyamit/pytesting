from django.db import models
from django.utils.timezone import now


class Company(models.Model):
    LAYOFF = "Layoff"
    HIRING = "Hiring"
    HIRING_FROZEN = "Hiring Frozen"
    STATUS_CHOICES = [
        (LAYOFF, "Layoff"),
        (HIRING, "Hiring"),
        (HIRING_FROZEN, "Hiring Frozen"),
    ]

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=HIRING)
    last_updated = models.DateTimeField(default=now, editable=True)
    application_link = models.URLField(blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
