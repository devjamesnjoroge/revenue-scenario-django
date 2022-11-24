from django.urls import include, path
from rest_framework import routers
from revenue import views

router = routers.DefaultRouter()
router.register(r'regions', views.RegionViewSet)
router.register(r'fiscal_countries', views.FiscalCountryViewSet)
router.register(r'industries', views.IndustryViewSet)
router.register(r'segments', views.SegmentViewSet)
router.register(r'currency_repositories', views.CurrencyRepositoryViewSet)
router.register(r'exchange_rate_libraries', views.ExchangeRateLibraryViewSet)
router.register(r'exchange_rate_has_current_repositories', views.ExchangeRateLibrary_has_CurrentRepositoryViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'product_types', views.ProductTypeViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'revenue_scenarios', views.RevenueScenarioViewSet)
router.register(r'revenue_scenario_has_products', views.RevenueScenarioHasProductViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    ]