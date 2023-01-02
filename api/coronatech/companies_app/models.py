from datetime import datetime
from django.db import models


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
    # last_updated = models.DateTimeField(null=True, blank=True)  #For both Date and time with editable option
    last_updated = models.DateField(
        null=True, blank=True
    )  # For only Date with editable option using django admin
    application_link = models.URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
