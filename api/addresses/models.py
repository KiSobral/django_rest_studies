from django.db import models


class Adress(models.Model):
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.line1
