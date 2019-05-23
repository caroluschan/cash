from django.db import models

# Create your models here.
class Player(models.Model):
    CASH_LIST = [10, 5, 2, 1, 0.5, 0.2, 0.1]
    cash = models.IntegerField(null=True, blank=True)