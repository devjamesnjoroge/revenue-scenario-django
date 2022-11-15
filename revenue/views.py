from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_regions(request):
    regions = Region.objects.all()
    serializer = RegionSerializer(regions, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_region(request):
    region_data = JSONParser().parse(request)
    region_serializer = RegionSerializer(data=region_data)
    if region_serializer.is_valid():
        region_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_fiscal_countries(request):
    fiscal_countries = FiscalCountry.objects.all()
    serializer = FiscalCountrySerializer(fiscal_countries, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_fiscal_country(request):
    fiscal_country_data = JSONParser().parse(request)
    fiscal_country_serializer = FiscalCountrySerializer(data=fiscal_country_data)
    if fiscal_country_serializer.is_valid():
        fiscal_country_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_industries(request):
    industries = Industry.objects.all()
    serializer = IndustrySerializer(industries, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_industry(request):
    industry_data = JSONParser().parse(request)
    industry_serializer = IndustrySerializer(data=industry_data)
    if industry_serializer.is_valid():
        industry_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_segments(request):
    segments = Segment.objects.all()
    serializer = SegmentSerializer(segments, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_segment(request):
    segment_data = JSONParser().parse(request)
    segment_serializer = SegmentSerializer(data=segment_data)
    if segment_serializer.is_valid():
        segment_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_currency_repositories(request):
    currency_repositories = CurrencyRepository.objects.all()
    serializer = CurrencyRepositorySerializer(currency_repositories, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_currency_repository(request):
    currency_repository_data = JSONParser().parse(request)
    currency_repository_serializer = CurrencyRepositorySerializer(data=currency_repository_data)
    if currency_repository_serializer.is_valid():
        currency_repository_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_exchange_rate_libraries(request):
    exchange_rate_libraries = ExchangeRateLibrary.objects.all()
    serializer = ExchangeRateLibrarySerializer(exchange_rate_libraries, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_exchange_rate_library(request):
    exchange_rate_library_data = JSONParser().parse(request)
    exchange_rate_library_serializer = ExchangeRateLibrarySerializer(data=exchange_rate_library_data)
    if exchange_rate_library_serializer.is_valid():
        exchange_rate_library_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_exchange_rate_has_current_repository(request):
    exchange_rate_has_current_repositories = Exchange_rate_has_current_repository.objects.all()
    serializer = Exchange_rate_has_current_repositorySerializer(exchange_rate_has_current_repositories, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_exchange_rate_has_current_repository(request):
    exchange_rate_has_current_repository_data = JSONParser().parse(request)
    exchange_rate_has_current_repository_serializer = Exchange_rate_has_current_repositorySerializer(data=exchange_rate_has_current_repository_data)
    if exchange_rate_has_current_repository_serializer.is_valid():
        exchange_rate_has_current_repository_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_project(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_project(request):
    project_data = JSONParser().parse(request)
    project_serializer = ProjectSerializer(data=project_data)
    if project_serializer.is_valid():
        project_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_product_type(request):
    product_types = ProductType.objects.all()
    serializer = ProductTypeSerializer(product_types, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_product_type(request):
    product_type_data = JSONParser().parse(request)
    product_type_serializer = ProductTypeSerializer(data=product_type_data)
    if product_type_serializer.is_valid():
        product_type_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_product(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_product(request):
    product_data = JSONParser().parse(request)
    product_serializer = ProductSerializer(data=product_data)
    if product_serializer.is_valid():
        product_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_revenue_scenario(request):
    revenue_scenarios = RevenueScenario.objects.all()
    serializer = RevenueScenarioSerializer(revenue_scenarios, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_revenue_scenario(request):
    revenue_scenario_data = JSONParser().parse(request)
    revenue_scenario_serializer = RevenueScenarioSerializer(data=revenue_scenario_data)
    if revenue_scenario_serializer.is_valid():
        revenue_scenario_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

def get_revenue_scenario_has_product(request):
    revenue_scenario_has_products = RevenueScenarioHasProduct.objects.all()
    serializer = RevenueScenarioHasProductSerializer(revenue_scenario_has_products, many=True)
    return JsonResponse(serializer.data, safe=False)

def post_revenue_scenario_has_product(request):
    revenue_scenario_has_product_data = JSONParser().parse(request)
    revenue_scenario_has_product_serializer = RevenueScenarioHasProductSerializer(data=revenue_scenario_has_product_data)
    if revenue_scenario_has_product_serializer.is_valid():
        revenue_scenario_has_product_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)

    
    

