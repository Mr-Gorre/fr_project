from django.db import models


class Deliver(models.Model):
    start_date = models.DateTimeField(null=False, blank=False)
    text = models.CharField(max_length=8000)
    filter = models.CharField(max_length=8000)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (
            f'"{self.text}" {self.start_date} - {self.end_date}, filter:{self.filter}'
        )


class Client(models.Model):
    phone = models.IntegerField(unique=True)
    provider_code = models.CharField(max_length=8000)
    tag = models.CharField(max_length=8000)
    time_zone = models.CharField(max_length=8000)

    def __str__(self):
        return f"{self.phone}, code: {self.provider_code}, tag: {self.tag}, at {self.time_zone}"


class Message(models.Model):

    CREATED = "created"
    COMPLETED = "completed"
    CANCELED = "canceled"
    EXPIRED = "expired"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    TO_REPEAT = "to_repeat"

    STATUS_CHOICES = [
        (CREATED, "Created"),
        (COMPLETED, "Succesfuly completed"),
        (CANCELED, "Canceled manualy"),
        (EXPIRED, "Expired by end time"),
        (FAILED, "Failed, wait for repeat"),
        (IN_PROGRESS, "Try sending"),
        (TO_REPEAT, "Marked to repeat manually"),
    ]

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=8000, choices=STATUS_CHOICES, default=CREATED)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    deliver = models.ForeignKey(Deliver, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Send "{self.deliver.text}" to {self.client}'
