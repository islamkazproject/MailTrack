from django.db import models
from django.utils import timezone


class Client(models.Model):
    phone_number = models.CharField(max_length=11)
    mobile_operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)


class Mailing(models.Model):
    start_datetime = models.DateTimeField(default=timezone.now)
    message_text = models.TextField()
    client_filter = models.Q()
    end_datetime = models.DateTimeField()

    def is_active(self):
        return self.start_datetime <= timezone.now() <= self.end_datetime


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


