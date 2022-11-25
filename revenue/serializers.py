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
        Region = serializers.PrimaryKeyRelatedField(many=True, queryset=Region.objects.all())
        fields = ("id", "FiscalCountryName", "Region", "FiscalCountryCode")

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ("id", "IndustryName")

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        Industry = serializers.PrimaryKeyRelatedField(read_only=False,many=True, queryset=Region.objects.all())
        fields = ("id", "SegmentName", "Industry")

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
        ExchangeRateLibrary = serializers.PrimaryKeyRelatedField(read_only=False,many=True, queryset=ExchangeRateLibrary.objects.all())
        CurrencyRepository = serializers.PrimaryKeyRelatedField(read_only=False,many=True, queryset=CurrencyRepository.objects.all())

        fields = ("id", "CurrencyRepository", "ExchangeRateLibrary")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        ExchangeRateLibrary = serializers.PrimaryKeyRelatedField(read_only=False,many=True, queryset=ExchangeRateLibrary.objects.all())
        ProjectCountry = serializers.PrimaryKeyRelatedField(read_only=False,many=True, queryset=FiscalCountry.objects.all())
        ProjectSegment = serializers.PrimaryKeyRelatedField(read_only=False,many=True, queryset=Segment.objects.all())

        fields = ("id", "ProjectName", "ProjectDesc", "ProjectCode", "ProjectCostCode", "ProjectStartDate", "ProjectEndDate", "ExchangeRateLibrary", "ProjectCountry", "ProjectSegment", "ProjectLocation")

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ("id", "ProductTypeName")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        ProductType = serializers.PrimaryKeyRelatedField(read_only=False,many=True, queryset=ProductType.objects.all())
        Project = serializers.PrimaryKeyRelatedField(read_only=False,many=True, queryset=Project.objects.all())

        fields = ("id", "ProductName", "ProductType", "Project")

class RevenueScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueScenario
        fields = ("id", "RevenueScenarioName")

class RevenueScenarioHasProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueScenarioHasProduct
        Product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
        RevenueScenario = serializers.PrimaryKeyRelatedField(many=True, queryset=RevenueScenario.objects.all())

        fields = ("id", "RevenueScenario", "RevenueYear", "RevenueUnitNumerator", "RevenueValue", "RevenueUnitDenominator",  "Product")

        

        

    



    