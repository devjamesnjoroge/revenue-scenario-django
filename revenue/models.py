from django.db import models

# Create your models here.

class Region(models.Model):
    RegionName = models.CharField(max_length=45)

    def __str__(self):
        return self.RegionName

class FiscalCountry(models.Model):
    FiscalCountryName = models.CharField(max_length=45)
    FiscalCountryCode = models.CharField(max_length=3)
    Region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.FiscalCountryName

class Industry(models.Model):
    IndustryName = models.CharField(max_length=45)

    def __str__(self):
        return self.IndustryName

class Segment(models.Model):
    SegmentName = models.CharField(max_length=45)
    Industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.SegmentName

class CurrencyRepository(models.Model):
    CurrencyName = models.CharField(max_length=45)
    CurrencyCode = models.CharField(max_length=45)

    def __str__(self):
        return self.CurrencyName

class ExchangeRateLibrary(models.Model):
    ExchangeRateLibraryName = models.FloatField(unique=True)
    CurrencyName = models.CharField(max_length=45, unique=True, )
    Year = models.DateField()
    ExchangeRateConversionValue = models.FloatField()
    def __str__(self):
        return self.ExchangeRateLibraryName

class ExchangeRateLibrary_has_CurrentRepository(models.Model):
    CurrencyRepository = models.ForeignKey(CurrencyRepository, on_delete=models.CASCADE)
    ExchangeRateLibrary = models.ForeignKey(ExchangeRateLibrary, on_delete=models.CASCADE)

    def __str__(self):
        return self.CurrencyRepository.CurrencyName

class Project(models.Model):
    ProjectName = models.CharField(max_length=45, unique=True)
    ProjectDescription = models.CharField(max_length=200)
    ProjectCode = models.CharField(max_length=10, unique=True)
    ProjectCostCode = models.CharField(max_length=20, unique=True)
    ProjectStartDate = models.DateField()
    ProjectEndDate = models.DateField()
    ProjectExchange_rate = models.ForeignKey(ExchangeRateLibrary, on_delete=models.CASCADE)
    ProjectCountry = models.ForeignKey(FiscalCountry, on_delete=models.CASCADE)
    ProjectSegment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    ProjectLocation = models.CharField(max_length=45)

    def __str__(self):
        return self.project_name

class ProductType(models.Model):
    product_type_name = models.CharField(max_length=45)

    def __str__(self):
        return self.product_type_name

class Product(models.Model):
    product_name = models.CharField(max_length=45)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class RevenueScenario(models.Model):
    revenue_scenario_name = models.CharField(max_length=45)

    def __str__(self):
        return self.revenue_scenario_name

class RevenueScenarioHasProduct(models.Model):
    revenue_scenario = models.ForeignKey(RevenueScenario, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    revenue_year = models.DateField()
    revenue_value = models.FloatField()
    revenue_unit_numerator = models.CharField(max_length=45)
    revenue_unit_denominator = models.CharField(max_length=45)

    def __str__(self):
        return self.revenue_scenario.revenue_scenario_name