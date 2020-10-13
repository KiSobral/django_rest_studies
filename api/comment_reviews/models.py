from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentary = models.TextField(null=False)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.commentary


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commentary = models.TextField(null=False)
    review = models.DecimalField(decimal_places=2, max_digits=3)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.review
