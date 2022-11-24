from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view
from .serializers import *

# @APIView GET, POST, DELETE, PUT

#Index page

def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST', 'DELETE'])
def Region_list(request):
     if request.method == 'GET':
          Regions = Region.objects.all()
          Regions_serializer = RegionSerializer(Regions, many=True)
          return JsonResponse(Regions_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          Region_data = JSONParser().parse(request)
          Region_serializer = RegionSerializer(data=Region_data)

          if Region_serializer.is_valid():
               Region_serializer.save()

               return JsonResponse(Region_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(Region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = Region.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Region detail

@api_view(['GET', 'PUT', 'DELETE'])
def Region_detail(request, pk):
     try: 
          Region = Region.objects.get(pk=pk) 
     except Region.DoesNotExist: 
          return JsonResponse({'message': 'The Region does not exist'}, status=status.HTTP_404_NOT_FOUND) 

     if request.method == 'GET': 
          Region_serializer = RegionSerializer(Region) 
          return JsonResponse(Region_serializer.data) 

     elif request.method == 'PUT': 
          Region_data = JSONParser().parse(request) 
          Region_serializer = RegionSerializer(Region, data=Region_data) 
          if Region_serializer.is_valid(): 
               Region_serializer.save() 
               return JsonResponse(Region_serializer.data) 
          return JsonResponse(Region_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

     elif request.method == 'DELETE': 
          Region.delete() 
          return JsonResponse({'message': 'Region was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def FiscalCountry_list(request):
     if request.method == 'GET':
          FiscalCountrys = FiscalCountry.objects.all()
          FiscalCountrys_serializer = FiscalCountrySerializer(FiscalCountrys, many=True)
          return JsonResponse(FiscalCountrys_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          FiscalCountry_data = JSONParser().parse(request)
          FiscalCountry_serializer = FiscalCountrySerializer(data=FiscalCountry_data)

          if FiscalCountry_serializer.is_valid():
               FiscalCountry_serializer.save()

               return JsonResponse(FiscalCountry_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(FiscalCountry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = FiscalCountry.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# FiscalCountry detail 

@api_view(['GET', 'PUT', 'DELETE'])
def FiscalCountry_detail(request, pk):
     try: 
          FiscalCountry = FiscalCountry.objects.get(pk=pk) 
     except FiscalCountry.DoesNotExist: 
          return JsonResponse({'message': 'The FiscalCountry does not exist'}, status=status.HTTP_404_NOT_FOUND) 

     if request.method == 'GET': 
          FiscalCountry_serializer = FiscalCountrySerializer(FiscalCountry) 
          return JsonResponse(FiscalCountry_serializer.data) 

     elif request.method == 'PUT': 
          FiscalCountry_data = JSONParser().parse(request) 
          FiscalCountry_serializer = FiscalCountrySerializer(FiscalCountry, data=FiscalCountry_data) 
          if FiscalCountry_serializer.is_valid(): 
               FiscalCountry_serializer.save() 
               return JsonResponse(FiscalCountry_serializer.data) 
          return JsonResponse(FiscalCountry_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

     elif request.method == 'DELETE': 
          FiscalCountry.delete() 
          return JsonResponse({'message': 'FiscalCountry was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def Industry_list(request):
     if request.method == 'GET':
          Industrys = Industry.objects.all()
          Industrys_serializer = IndustrySerializer(Industrys, many=True)
          return JsonResponse(Industrys_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          Industry_data = JSONParser().parse(request)
          Industry_serializer = IndustrySerializer(data=Industry_data)

          if Industry_serializer.is_valid():
               Industry_serializer.save()

               return JsonResponse(Industry_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(Industry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = Industry.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Industry detail

@api_view(['GET', 'PUT', 'DELETE'])
def Industry_detail(request, pk):
     try: 
          Industry = Industry.objects.get(pk=pk) 
     except Industry.DoesNotExist: 
          return JsonResponse({'message': 'The Industry does not exist'}, status=status.HTTP_404_NOT_FOUND) 

     if request.method == 'GET': 
          Industry_serializer = IndustrySerializer(Industry) 
          return JsonResponse(Industry_serializer.data) 

     elif request.method == 'PUT': 
          Industry_data = JSONParser().parse(request) 
          Industry_serializer = IndustrySerializer(Industry, data=Industry_data) 
          if Industry_serializer.is_valid(): 
               Industry_serializer.save() 
               return JsonResponse(Industry_serializer.data) 
          return JsonResponse(Industry_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

     elif request.method == 'DELETE': 
          Industry.delete() 
          return JsonResponse({'message': 'Industry was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def Segment_list(request):
     if request.method == 'GET':
          Segments = Segment.objects.all()
          Segments_serializer = SegmentSerializer(Segments, many=True)
          return JsonResponse(Segments_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          Segment_data = JSONParser().parse(request)
          Segment_serializer = SegmentSerializer(data=Segment_data)

          if Segment_serializer.is_valid():
               Segment_serializer.save()

               return JsonResponse(Segment_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(Segment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = Segment.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Segment detail

@api_view(['GET', 'PUT', 'DELETE'])
def Segment_detail(request, pk):
     try: 
          Segment = Segment.objects.get(pk=pk) 
     except Segment.DoesNotExist: 
          return JsonResponse({'message': 'The Segment does not exist'}, status=status.HTTP_404_NOT_FOUND) 

     if request.method == 'GET': 
          Segment_serializer = SegmentSerializer(Segment) 
          return JsonResponse(Segment_serializer.data) 

     elif request.method == 'PUT': 
          Segment_data = JSONParser().parse(request) 
          Segment_serializer = SegmentSerializer(Segment, data=Segment_data) 
          if Segment_serializer.is_valid(): 
               Segment_serializer.save() 
               return JsonResponse(Segment_serializer.data) 
          return JsonResponse(Segment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

     elif request.method == 'DELETE': 
          Segment.delete() 
          return JsonResponse({'message': 'Segment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def CurrencyRepository_list(request):
     if request.method == 'GET':
          CurrencyRepositorys = CurrencyRepository.objects.all()
          CurrencyRepositorys_serializer = CurrencyRepositorySerializer(CurrencyRepositorys, many=True)
          return JsonResponse(CurrencyRepositorys_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          CurrencyRepository_data = JSONParser().parse(request)
          CurrencyRepository_serializer = CurrencyRepositorySerializer(data=CurrencyRepository_data)

          if CurrencyRepository_serializer.is_valid():
               CurrencyRepository_serializer.save()

               return JsonResponse(CurrencyRepository_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(CurrencyRepository_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = CurrencyRepository.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# CurrencyRepository detail

@api_view(['GET', 'PUT', 'DELETE'])
def CurrencyRepository_detail(request, pk):
     try: 
          CurrencyRepository = CurrencyRepository.objects.get(pk=pk) 
     except CurrencyRepository.DoesNotExist: 
          return JsonResponse({'message': 'The CurrencyRepository does not exist'}, status=status.HTTP_404_NOT_FOUND) 

     if request.method == 'GET': 
          CurrencyRepository_serializer = CurrencyRepositorySerializer(CurrencyRepository) 
          return JsonResponse(CurrencyRepository_serializer.data) 

     elif request.method == 'PUT': 
          CurrencyRepository_data = JSONParser().parse(request) 
          CurrencyRepository_serializer = CurrencyRepositorySerializer(CurrencyRepository, data=CurrencyRepository_data) 
          if CurrencyRepository_serializer.is_valid(): 
               CurrencyRepository_serializer.save() 
               return JsonResponse(CurrencyRepository_serializer.data) 
          return JsonResponse(CurrencyRepository_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

     elif request.method == 'DELETE': 
          CurrencyRepository.delete() 
          return JsonResponse({'message': 'CurrencyRepository was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def ExchangeRateLibrary_list(request):
     if request.method == 'GET':
          ExchangeRateLibrarys = ExchangeRateLibrary.objects.all()
          ExchangeRateLibrarys_serializer = ExchangeRateLibrarySerializer(ExchangeRateLibrarys, many=True)
          return JsonResponse(ExchangeRateLibrarys_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          ExchangeRateLibrary_data = JSONParser().parse(request)
          ExchangeRateLibrary_serializer = ExchangeRateLibrarySerializer(data=ExchangeRateLibrary_data)

          if ExchangeRateLibrary_serializer.is_valid():
               ExchangeRateLibrary_serializer.save()

               return JsonResponse(ExchangeRateLibrary_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(ExchangeRateLibrary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = ExchangeRateLibrary.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# ExchangeRateLibrary detail

@api_view(['GET', 'PUT', 'DELETE'])
def ExchangeRateLibrary_detail(request, pk):
     
     try: 
          ExchangeRateLibrary = ExchangeRateLibrary.objects.get(pk=pk) 
     except ExchangeRateLibrary.DoesNotExist: 
          return JsonResponse({'message': 'The Exchange Rate Library does not exist'}, status=status.HTTP_404_NOT_FOUND)

     if request.method == 'GET':
          ExchangeRateLibrary_serializer = ExchangeRateLibrarySerializer(ExchangeRateLibrary)
          return JsonResponse(ExchangeRateLibrary_serializer.data)

     elif request.method == 'PUT':
          ExchangeRateLibrary_data = JSONParser().parse(request)
          ExchangeRateLibrary_serializer = ExchangeRateLibrarySerializer(ExchangeRateLibrary, data=ExchangeRateLibrary_data)
          if ExchangeRateLibrary_serializer.is_valid():
               ExchangeRateLibrary_serializer.save()
               return JsonResponse(ExchangeRateLibrary_serializer.data)
          return JsonResponse(ExchangeRateLibrary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          ExchangeRateLibrary.delete()
          return JsonResponse({'message': 'Exchange Rate Library was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def ExchangeRateLibrary_has_CurrentRepository_list(request):
     if request.method == 'GET':
          ExchangeRateLibrary_has_CurrentRepositorys = ExchangeRateLibrary_has_CurrentRepository.objects.all()
          ExchangeRateLibrary_has_CurrentRepositorys_serializer = ExchangeRateLibrary_has_CurrentRepositorySerializer(ExchangeRateLibrary_has_CurrentRepositorys, many=True)
          return JsonResponse(ExchangeRateLibrary_has_CurrentRepositorys_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          ExchangeRateLibrary_has_CurrentRepository_data = JSONParser().parse(request)
          ExchangeRateLibrary_has_CurrentRepository_serializer = ExchangeRateLibrary_has_CurrentRepositorySerializer(data=ExchangeRateLibrary_has_CurrentRepository_data)

          if ExchangeRateLibrary_has_CurrentRepository_serializer.is_valid():
               ExchangeRateLibrary_has_CurrentRepository_serializer.save()

               return JsonResponse(ExchangeRateLibrary_has_CurrentRepository_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(ExchangeRateLibrary_has_CurrentRepository_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = ExchangeRateLibrary_has_CurrentRepository.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# ExchangeRateLibrary_has_CurrentRepository detail

@api_view(['GET', 'PUT', 'DELETE'])
def ExchangeRateLibrary_has_CurrentRepository_detail(request, pk):
          
          try: 
               ExchangeRateLibrary_has_CurrentRepository = ExchangeRateLibrary_has_CurrentRepository.objects.get(pk=pk) 
          except ExchangeRateLibrary_has_CurrentRepository.DoesNotExist: 
               return JsonResponse({'message': 'The Exchange Rate Library has Currency Repository does not exist'}, status=status.HTTP_404_NOT_FOUND)
     
          if request.method == 'GET':
               ExchangeRateLibrary_has_CurrentRepository_serializer = ExchangeRateLibrary_has_CurrentRepositorySerializer(ExchangeRateLibrary_has_CurrentRepository)
               return JsonResponse(ExchangeRateLibrary_has_CurrentRepository_serializer.data)
     
          elif request.method == 'PUT':
               ExchangeRateLibrary_has_CurrentRepository_data = JSONParser().parse(request)
               ExchangeRateLibrary_has_CurrentRepository_serializer = ExchangeRateLibrary_has_CurrentRepositorySerializer(ExchangeRateLibrary_has_CurrentRepository, data=ExchangeRateLibrary_has_CurrentRepository_data)
               if ExchangeRateLibrary_has_CurrentRepository_serializer.is_valid():
                    ExchangeRateLibrary_has_CurrentRepository_serializer.save()
                    return JsonResponse(ExchangeRateLibrary_has_CurrentRepository_serializer.data)
               return JsonResponse(ExchangeRateLibrary_has_CurrentRepository_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
          elif request.method == 'DELETE':
               ExchangeRateLibrary_has_CurrentRepository.delete()
               return JsonResponse({'message': 'Exchange Rate Library has Currency Repository was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def Project_list(request):
     if request.method == 'GET':
          Projects = Project.objects.all()
          Projects_serializer = ProjectSerializer(Projects, many=True)
          return JsonResponse(Projects_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          Project_data = JSONParser().parse(request)
          Project_serializer = ProjectSerializer(data=Project_data)

          if Project_serializer.is_valid():
               Project_serializer.save()

               return JsonResponse(Project_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(Project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = Project.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Project detail

@api_view(['GET', 'PUT', 'DELETE'])
def Project_detail(request, pk):
          
          try: 
               Project = Project.objects.get(pk=pk) 
          except Project.DoesNotExist: 
               return JsonResponse({'message': 'The Project does not exist'}, status=status.HTTP_404_NOT_FOUND)
     
          if request.method == 'GET':
               Project_serializer = ProjectSerializer(Project)
               return JsonResponse(Project_serializer.data)
     
          elif request.method == 'PUT':
               Project_data = JSONParser().parse(request)
               Project_serializer = ProjectSerializer(Project, data=Project_data)
               if Project_serializer.is_valid():
                    Project_serializer.save()
                    return JsonResponse(Project_serializer.data)
               return JsonResponse(Project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
          elif request.method == 'DELETE':
               Project.delete()
               return JsonResponse({'message': 'Project was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def ProductType_list(request):
     if request.method == 'GET':
          ProductTypes = ProductType.objects.all()
          ProductTypes_serializer = ProductTypeSerializer(ProductTypes, many=True)
          return JsonResponse(ProductTypes_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          ProductType_data = JSONParser().parse(request)
          ProductType_serializer = ProductTypeSerializer(data=ProductType_data)

          if ProductType_serializer.is_valid():
               ProductType_serializer.save()

               return JsonResponse(ProductType_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(ProductType_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = ProductType.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# ProductType detail

@api_view(['GET', 'PUT', 'DELETE'])
def ProductType_detail(request, pk):

          try: 
               ProductType = ProductType.objects.get(pk=pk) 
          except ProductType.DoesNotExist: 
               return JsonResponse({'message': 'The Product Type does not exist'}, status=status.HTTP_404_NOT_FOUND)
     
          if request.method == 'GET':
               ProductType_serializer = ProductTypeSerializer(ProductType)
               return JsonResponse(ProductType_serializer.data)
     
          elif request.method == 'PUT':
               ProductType_data = JSONParser().parse(request)
               ProductType_serializer = ProductTypeSerializer(ProductType, data=ProductType_data)
               if ProductType_serializer.is_valid():
                    ProductType_serializer.save()
                    return JsonResponse(ProductType_serializer.data)
               return JsonResponse(ProductType_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
          elif request.method == 'DELETE':
               ProductType.delete()
               return JsonResponse({'message': 'Product Type was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def Product_list(request):
     if request.method == 'GET':
          Products = Product.objects.all()
          Products_serializer = ProductSerializer(Products, many=True)
          return JsonResponse(Products_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          Product_data = JSONParser().parse(request)
          Product_serializer = ProductSerializer(data=Product_data)

          if Product_serializer.is_valid():
               Product_serializer.save()

               return JsonResponse(Product_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(Product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = Product.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Product detail

@api_view(['GET', 'PUT', 'DELETE'])
def Product_detail(request, pk):
     
               try: 
                    Product = Product.objects.get(pk=pk) 
               except Product.DoesNotExist: 
                    return JsonResponse({'message': 'The Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
          
               if request.method == 'GET':
                    Product_serializer = ProductSerializer(Product)
                    return JsonResponse(Product_serializer.data)
          
               elif request.method == 'PUT':
                    Product_data = JSONParser().parse(request)
                    Product_serializer = ProductSerializer(Product, data=Product_data)
                    if Product_serializer.is_valid():
                         Product_serializer.save()
                         return JsonResponse(Product_serializer.data)
                    return JsonResponse(Product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
               elif request.method == 'DELETE':
                    Product.delete()
                    return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def RevenueScenario_list(request):
     if request.method == 'GET':
          RevenueScenarios = RevenueScenario.objects.all()
          RevenueScenarios_serializer = RevenueScenarioSerializer(RevenueScenarios, many=True)
          return JsonResponse(RevenueScenarios_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          RevenueScenario_data = JSONParser().parse(request)
          RevenueScenario_serializer = RevenueScenarioSerializer(data=RevenueScenario_data)

          if RevenueScenario_serializer.is_valid():
               RevenueScenario_serializer.save()

               return JsonResponse(RevenueScenario_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(RevenueScenario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = RevenueScenario.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# RevenueScenario detail

@api_view(['GET', 'PUT', 'DELETE'])
def RevenueScenario_detail(request, pk):
          
                    try: 
                         RevenueScenario = RevenueScenario.objects.get(pk=pk) 
                    except RevenueScenario.DoesNotExist: 
                         return JsonResponse({'message': 'The Revenue Scenario does not exist'}, status=status.HTTP_404_NOT_FOUND)
               
                    if request.method == 'GET':
                         RevenueScenario_serializer = RevenueScenarioSerializer(RevenueScenario)
                         return JsonResponse(RevenueScenario_serializer.data)
               
                    elif request.method == 'PUT':
                         RevenueScenario_data = JSONParser().parse(request)
                         RevenueScenario_serializer = RevenueScenarioSerializer(RevenueScenario, data=RevenueScenario_data)
                         if RevenueScenario_serializer.is_valid():
                              RevenueScenario_serializer.save()
                              return JsonResponse(RevenueScenario_serializer.data)
                         return JsonResponse(RevenueScenario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
               
                    elif request.method == 'DELETE':
                         RevenueScenario.delete()
                         return JsonResponse({'message': 'Revenue Scenario was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def RevenueScenarioHasProduct_list(request):
     if request.method == 'GET':
          RevenueScenarioHasProducts = RevenueScenarioHasProduct.objects.all()
          RevenueScenarioHasProducts_serializer = RevenueScenarioHasProductSerializer(RevenueScenarioHasProducts, many=True)
          return JsonResponse(RevenueScenarioHasProducts_serializer.data, safe=False)
          # 'safe=False' for objects serialization

     elif request.method == 'POST':
          RevenueScenarioHasProduct_data = JSONParser().parse(request)
          RevenueScenarioHasProduct_serializer = RevenueScenarioHasProductSerializer(data=RevenueScenarioHasProduct_data)

          if RevenueScenarioHasProduct_serializer.is_valid():
               RevenueScenarioHasProduct_serializer.save()

               return JsonResponse(RevenueScenarioHasProduct_serializer.data, status=status.HTTP_201_CREATED)

          return JsonResponse(RevenueScenarioHasProduct_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     elif request.method == 'DELETE':
          count = RevenueScenarioHasProduct.objects.all().delete()
          return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# RevenueScenarioHasProduct detail

@api_view(['GET', 'PUT', 'DELETE'])
def RevenueScenarioHasProduct_detail(request, pk):
               
                         try: 
                              RevenueScenarioHasProduct = RevenueScenarioHasProduct.objects.get(pk=pk) 
                         except RevenueScenarioHasProduct.DoesNotExist: 
                              return JsonResponse({'message': 'The Revenue Scenario Has Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
                    
                         if request.method == 'GET':
                              RevenueScenarioHasProduct_serializer = RevenueScenarioHasProductSerializer(RevenueScenarioHasProduct)
                              return JsonResponse(RevenueScenarioHasProduct_serializer.data)
                    
                         elif request.method == 'PUT':
                              RevenueScenarioHasProduct_data = JSONParser().parse(request)
                              RevenueScenarioHasProduct_serializer = RevenueScenarioHasProductSerializer(RevenueScenarioHasProduct, data=RevenueScenarioHasProduct_data)
                              if RevenueScenarioHasProduct_serializer.is_valid():
                                   RevenueScenarioHasProduct_serializer.save()
                                   return JsonResponse(RevenueScenarioHasProduct_serializer.data)
                              return JsonResponse(RevenueScenarioHasProduct_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                         elif request.method == 'DELETE':
                              RevenueScenarioHasProduct.delete()
                              return JsonResponse({'message': 'Revenue Scenario Has Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
