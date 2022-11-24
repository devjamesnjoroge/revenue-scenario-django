# import serializers
from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "RegionName")

class FiscalCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalCountry
        fields = ("id", "FiscalCountryName", "Region_id", "FiscalCountryCode")

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ("id", "IndustryName")

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ("id", "SegmentName", "Industry_id")

class CurrencyRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRepository
        fields = ("id", "CurrencyName", "CurrencyCode")

class ExchangeRateLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateLibrary
        fields = ("id", "ExchangeRateLibraryName", "CurrencyName", "Year", "ExchangeRateConversionValue")

class ExchangeRateLibrary_has_CurrentRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateLibrary_has_CurrentRepository
        fields = ("id", "CurrencyRepository_id", "ExchangeRateLibrary_id")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "ProjectName", "ProjectDesc", "ProjectCode", "ProjectCostCode", "ProjectStartDate", "ProjectEndDate", "ExchangeRateLibrary_id")

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ("id", "ProductTypeName")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "ProductName", "ProductType_id")

class RevenueScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueScenario
        fields = ("id", "RevenueScenarioName")

class RevenueScenarioHasProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueScenarioHasProduct
        fields = ("id", "RevenueScenario_id", "Product_id", "RevenueYear", "RevenueUnitNumerator", "RevenueValue", "RevenueUnitDenominator")

        

        

    



    