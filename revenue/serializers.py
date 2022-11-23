# import serializers
from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class FiscalCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalCountry
        fields = "__all__"

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = "__all__"

class CurrencyRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRepository
        fields = "__all__"

class ExchangeRateLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateLibrary
        fields = "__all__"

class Exchange_rate_has_current_repositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateLibrary_has_CurrentRepository
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class RevenueScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueScenario
        fields = "__all__"

class RevenueScenarioHasProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueScenarioHasProduct
        fields = "__all__"



    