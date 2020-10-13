from django.db import models
from attractions.models import Attraction
from comment_reviews.models import Comment, Review
from addresses.models import Adress


class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approvedd = models.BooleanField(default=True)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    adress = models.ForeignKey(
        Adress, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
