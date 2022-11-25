from django.urls import path,include
from . import views
#Import routers
from rest_framework import routers

# Router for API endpoints
router = routers.DefaultRouter()

# Register API endpoints
router.register(r'region', views.RegionViewSet)
router.register(r'fiscalcountry', views.FiscalCountryViewSet)
router.register(r'industry', views.IndustryViewSet)
router.register(r'segment', views.SegmentViewSet)
router.register(r'currencyrepository', views.CurrencyRepositoryViewSet)
router.register(r'exchangeratelibrary', views.ExchangeRateLibraryViewSet)
router.register(r'exchangeratelibrary_has_currentrepository', views.ExchangeRateLibrary_has_CurrentRepositoryViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'revenuescenario', views.RevenueScenarioViewSet)
router.register(r'revenuescenarioHasProduct', views.RevenueScenarioHasProductViewSet)

urlpatterns = [

    path('', views.index, name='index'),

    path('api/', include(router.urls)),
]