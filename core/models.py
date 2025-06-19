from django.db import models


class HotWheelsModel(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    series = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self):
        return f"{self.name} ({self.year})"
