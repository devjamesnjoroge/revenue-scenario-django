# LIST CREATE API VIEW WITH GENERIC CLASS BASED VIEWS GET, POST, PUT, PATCH, DELETE

from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from .models import Region, FiscalCountry, Industry, Segment, CurrencyRepository, ExchangeRateLibrary, ExchangeRateLibrary_has_CurrentRepository, Project, ProductType, Product, RevenueScenario, RevenueScenarioHasProduct
from .serializers import RegionSerializer, FiscalCountrySerializer, IndustrySerializer, SegmentSerializer, CurrencyRepositorySerializer, ExchangeRateLibrarySerializer, ExchangeRateLibrary_has_CurrentRepositorySerializer, ProjectSerializer, ProductTypeSerializer, ProductSerializer, RevenueScenarioSerializer, RevenueScenarioHasProductSerializer
# import render to html
from django.shortcuts import render

# Create your views here.

# API endpoints

def index(request):
    return render(request, 'index.html')

class RegionViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = Region.objects.all()
     serializer_class = RegionSerializer

class FiscalCountryViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = FiscalCountry.objects.all()
     serializer_class = FiscalCountrySerializer

class IndustryViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = Industry.objects.all()
     serializer_class = IndustrySerializer

class SegmentViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = Segment.objects.all()
     serializer_class = SegmentSerializer

class CurrencyRepositoryViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = CurrencyRepository.objects.all()
     serializer_class = CurrencyRepositorySerializer

class ExchangeRateLibraryViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = ExchangeRateLibrary.objects.all()
     serializer_class = ExchangeRateLibrarySerializer

class ExchangeRateLibrary_has_CurrentRepositoryViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = ExchangeRateLibrary_has_CurrentRepository.objects.all()
     serializer_class = ExchangeRateLibrary_has_CurrentRepositorySerializer

class ProjectViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = Project.objects.all()
     serializer_class = ProjectSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = ProductType.objects.all()
     serializer_class = ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

class RevenueScenarioViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = RevenueScenario.objects.all()
     serializer_class = RevenueScenarioSerializer

class RevenueScenarioHasProductViewSet(viewsets.ModelViewSet):
     """
     This viewset automatically provides `list`, `create`, `retrieve`,
     `update` and `destroy` actions.
     """
     queryset = RevenueScenarioHasProduct.objects.all()
     serializer_class = RevenueScenarioHasProductSerializer
