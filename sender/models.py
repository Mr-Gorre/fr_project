from django.db import models


class Deliver(models.Model):
  start_date = models.DateTimeField()
  text = models.CharField(max_length=8000)
  filter = models.CharField(max_length=8000)
  end_date = models.DateTimeField()


class Client(models.Model):
  phone = models.IntegerField()
  provider_code = models.CharField(max_length=8000)
  tag = models.CharField(max_length=8000)
  time_zone = models.CharField(max_length=8000)

class Message(models.Model):
  created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
  status = models.CharField(max_length=8000)
  client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
  deliver = models.ForeignKey(Deliver, on_delete=models.SET_NULL, null=True)
