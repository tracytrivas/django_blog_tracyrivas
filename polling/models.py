from django.db import models


# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"This one is {self.title}"

