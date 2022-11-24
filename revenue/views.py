# Imports for GET, POST, PUT, DELETE methods for API
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Import models
from .models import *
# Import serializers
from .serializers import *

# Create your views here.

class RegionViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Region.objects.all
    serializer_class = RegionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FiscalCountryViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
     queryset = FiscalCountry.objects.all
     serializer_class = FiscalCountrySerializer
    
     def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
    
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)


class IndustryViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
     queryset = Industry.objects.all
     serializer_class = IndustrySerializer
    
     def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
    
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)


class SegmentViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
     queryset = Segment.objects.all
     serializer_class = SegmentSerializer
    
     def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
    
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)


class CurrencyRepositoryViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.GenericAPIView):
     queryset = CurrencyRepository.objects.all
     serializer_class = CurrencyRepositorySerializer
    
     def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
    
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)


class ExchangeRateLibraryViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.GenericAPIView):
     queryset = ExchangeRateLibrary.objects.all
     serializer_class = ExchangeRateLibrarySerializer
    
     def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
    
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)


class ExchangeRateLibrary_has_CurrentRepositoryViewSet(mixins.ListModelMixin,
                                                        mixins.CreateModelMixin,
                                                        mixins.RetrieveModelMixin,
                                                        mixins.UpdateModelMixin,
                                                        mixins.DestroyModelMixin,
                                                        generics.GenericAPIView):
     queryset = ExchangeRateLibrary_has_CurrentRepository
     serializer_class = ExchangeRateLibrary_has_CurrentRepositorySerializer

     def get(self, request, *args, **kwargs):
         return self.list(request, *args, **kwargs)
        
     def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)


class Project(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
     queryset = Project.objects.all
     serializer_class = ProjectSerializer
    
     def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
    
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)

class ProductTypeViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
     queryset = ProductType.objects.all
     serializer_class = ProductTypeSerializer
    
     def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
    
     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)


# Product view. 
class ProductViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
     queryset = Product.objects.all
     serializer_class = ProductSerializer

     def get(self, request, *args, **kwargs):
         return self.list(request, *args, **kwargs)

     def post(self, request, *args, **kwargs):
         return self