from django.db import models


class EmailStatus(models.TextChoices):

    SENT = "SENT", "sent"
    FAILED = "NOT_SENT", "failed"