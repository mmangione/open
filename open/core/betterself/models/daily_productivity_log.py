from django.db.models import CharField, DateField, PositiveIntegerField, TextField

from open.core.betterself.constants import INPUT_SOURCES_TUPLES
from open.utilities.models import BaseModelWithUserGeneratedContent


class DailyProductivityLog(BaseModelWithUserGeneratedContent):
    """
    Represents the daily over-view of how productive a user was on that day, mimics
    RescueTime's concept of productive time, mildly productive, etc.
    """

    source = CharField(max_length=50, choices=INPUT_SOURCES_TUPLES)
    date = DateField()

    very_productive_time_minutes = PositiveIntegerField(null=True, blank=True)
    productive_time_minutes = PositiveIntegerField(null=True, blank=True)
    neutral_time_minutes = PositiveIntegerField(null=True, blank=True)
    distracting_time_minutes = PositiveIntegerField(null=True, blank=True)
    very_distracting_time_minutes = PositiveIntegerField(null=True, blank=True)
    notes = TextField(default="")

    class Meta:
        verbose_name = "Daily Productivity Log"
        verbose_name_plural = "Daily Productivity Logs"
        unique_together = (("date", "user"),)
        ordering = ["-date"]

    def __str__(self):
        return "{} Productivity Log".format(self.date)
