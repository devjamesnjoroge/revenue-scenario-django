from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('region/', views.RegionViewSet.as_view(), name='region'),
    path('fiscalcountry/', views.FiscalCountryViewSet.as_view(), name='fiscalcountry'),
    path('industry/', views.IndustryViewSet.as_view(), name='industry'),
    path('segment/', views.SegmentViewSet.as_view(), name='segment'),
    path('currencyrepository/', views.CurrencyRepositoryViewSet.as_view(), name='currencyrepository'),
    path('exchangeratelibrary/', views.ExchangeRateLibraryViewSet.as_view(), name='exchangeratelibrary'),
    path('exchange_rate_has_current_repository/', views.Exchange_rate_has_current_repositoryViewSet.as_view(), name='exchange_rate_has_current_repository'),
    path('project/', views.ProjectViewSet.as_view(), name='project'),
    path('producttype/', views.ProductTypeViewSet.as_view(), name='producttype'),
    path('product/', views.ProductViewSet.as_view(), name='product'),
    path('revenuescenario/', views.RevenueScenarioViewSet.as_view(), name='revenuescenario'),
    path('revenuescenariohasproduct/', views.RevenueScenarioHasProductViewSet.as_view(), name='revenuescenariohasproduct'),
    
]