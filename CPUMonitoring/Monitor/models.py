from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Utilisation(models.Model):
    date_time=models.DateTimeField(unique=True,default=timezone.now)
    cpu_usage=models.FloatField()
    ram_usage=models.FloatField()


    def __str__(self):
        return str(self.date_time)
