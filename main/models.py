from django.db import models


# Create your models here.
class Competitor(models.Model):
    Competitor_Logo = models.FileField()
    Competitor_Name = models.CharField(max_length=200)
    Competitor_Website = models.CharField(max_length=200)
    Notes = models.TextField(max_length=100000)
    Twitter = models.CharField(max_length=200, blank=True)
    Facebook = models.CharField(max_length=200, blank=True)
    LinkedIn = models.CharField(max_length=200, blank=True)
    Category = models.CharField(max_length=200, blank=True)
    Crunchbase = models.CharField(max_length=200, blank=True)
    Similarweb = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.Competitor_Name
