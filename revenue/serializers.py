# import serializers
from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('region_name',)

class FiscalCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalCountry
        fields = ('country_name', 'country_code', 'region')

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('industry_name',)

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ('segment_name', 'industry')

class CurrencyRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRepository
        fields = ('currency_name', 'currency_code')

class ExchangeRateLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateLibrary
        fields = ('currency', 'exchange_rate', 'exchange_rate_date', 'exchange_rate_conversion_value')

class Exchange_rate_has_current_repositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange_rate_has_current_repository
        fields = ('currency', 'exchange_rate')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name', 'project_description', 'project_code', 'project_cost_code', 'project_start_date', 'project_end_date', 'project_exchange_rate', 'project_country')

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('product_type_name',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_type', 'product_segment')

class RevenueScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueScenario
        fields = ('revenue_scenario_name', 'revenue_scenario_description', 'revenue_scenario_start_date', 'revenue_scenario_end_date', 'revenue_scenario_project')

class RevenueScenarioHasProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueScenarioHasProduct
        fields = ('revenue_scenario', 'product')

        

    