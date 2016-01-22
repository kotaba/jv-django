from django.db import models
from django.contrib.auth.models import User

class TeamInboundSale(models.Model):
    name = models.CharField(max_length=100)
    tickets = models.IntegerField()