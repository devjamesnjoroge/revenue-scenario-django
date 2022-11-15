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

class Industry(models.Model):
    industry_name = models.CharField(max_length=50)

    def __str__(self):
        return self.industry_name

class Segment(models.Model):
    segment_name = models.CharField(max_length=50)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.segment_name

class CurrencyRepository(models.Model):
    currency_name = models.CharField(max_length=50)
    currency_code = models.CharField(max_length=3)

    def __str__(self):
        return self.currency_name

class ExchangeRateLibrary(models.Model):
    currency = models.ForeignKey(CurrencyRepository, on_delete=models.CASCADE)
    exchange_rate = models.FloatField()
    exchange_rate_date = models.DateField()
    exchange_rate_conversion_value = models.FloatField()

    def __str__(self):
        return self.currency.currency_name

class Exchange_rate_has_current_repository(models.Model):
    currency = models.ForeignKey(CurrencyRepository, on_delete=models.CASCADE)
    exchange_rate = models.ForeignKey(ExchangeRateLibrary, on_delete=models.CASCADE)

    def __str__(self):
        return self.currency.currency_name

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=200)
    project_code = models.CharField(max_length=50)
    project_cost_code = models.CharField(max_length=50)
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    project_exchange_rate = models.ForeignKey(ExchangeRateLibrary, on_delete=models.CASCADE)
    project_country = models.ForeignKey(FiscalCountry, on_delete=models.CASCADE)
    project_segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    project_location = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name