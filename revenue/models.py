from django.db import models

# Create your models here.

class Region(models.Model):
    region_name = models.CharField(max_length=50)

    def __str__(self):
        return self.region_name

class FiscalCountry(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=3)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name