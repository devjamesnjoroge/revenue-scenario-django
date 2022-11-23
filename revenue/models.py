from django.db import models

# Create your models here.

class Region(models.Model):
    RegionName = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.RegionName

class FiscalCountry(models.Model):
    FiscalCountryName = models.CharField(max_length=45, unique=True)
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
    CurrencyName = models.CharField(max_length=45, unique=True)
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
    ProjectDesc = models.CharField(max_length=200)
    ProjectCode = models.CharField(max_length=10, unique=True)
    ProjectCostCode = models.CharField(max_length=20, unique=True)
    ProjectStartDate = models.DateField()
    ProjectEndDate = models.DateField()
    ExchangeRateLibrary = models.ForeignKey(ExchangeRateLibrary, on_delete=models.CASCADE)
    ProjectCountry = models.ForeignKey(FiscalCountry, on_delete=models.CASCADE)
    ProjectSegment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    ProjectLocation = models.CharField(max_length=45)

    def __str__(self):
        return self.ProjectName

class ProductType(models.Model):
    ProductTypeName = models.CharField(max_length=45)

    def __str__(self):
        return self.ProductTypeName

class Product(models.Model):
    ProductName = models.CharField(max_length=45)
    ProductType = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProductName

class RevenueScenario(models.Model):
    RevenueScenarioName = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.RevenueScenarioName

class RevenueScenarioHasProduct(models.Model):
    RevenueScenario = models.ForeignKey(RevenueScenario, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    RevenueYear = models.DateField()
    RevenueValue = models.FloatField()
    RevenueUnitNumerator = models.CharField(max_length=45)
    RevenueUnitDenominator = models.CharField(max_length=45)

    def __str__(self):
        return self.RevenueScenario.RevenueScenarioName