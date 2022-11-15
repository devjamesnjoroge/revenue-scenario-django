from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

def index(request):
    return render(request, 'index.html')

class RegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Region.objects.all().order_by('id')
    serializer_class = RegionSerializer

class FiscalCountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FiscalCountry.objects.all().order_by('id')
    serializer_class = FiscalCountrySerializer

class IndustryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Industry.objects.all().order_by('id')
    serializer_class = IndustrySerializer

class SegmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Segment.objects.all().order_by('id')
    serializer_class = SegmentSerializer

class CurrencyRepositoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CurrencyRepository.objects.all().order_by('id')
    serializer_class = CurrencyRepositorySerializer

class ExchangeRateLibraryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExchangeRateLibrary.objects.all().order_by('id')
    serializer_class = ExchangeRateLibrarySerializer

class Exchange_rate_has_current_repositoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exchange_rate_has_current_repository.objects.all().order_by('id')
    serializer_class = Exchange_rate_has_current_repositorySerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProductType.objects.all().order_by('id')
    serializer_class = ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class RevenueScenarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RevenueScenario.objects.all().order_by('id')
    serializer_class = RevenueScenarioSerializer

class RevenueScenarioHasProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RevenueScenarioHasProduct.objects.all().order_by('id')
    serializer_class = RevenueScenarioHasProductSerializer
