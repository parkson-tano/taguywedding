from django.db import models

# Create your models here.


class Invite(models.Model):
    name = models.CharField(max_length=100)
    table = models.CharField(max_length=100)
    arrived = models.BooleanField(default=False)
    time_of_arrival = models.DateTimeField()

    def __str__(self):
        return f'{self.name} at {self.table}'
