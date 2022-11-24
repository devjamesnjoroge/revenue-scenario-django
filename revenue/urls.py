from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('region/', views.Region_list, name='Region_list'),
    path('region/<int:pk>/', views.Region_detail, name='Region_detail'),
    path('fiscalcountry/', views.FiscalCountry_list, name='FiscalCountry_list'),
    path('fiscalcountry/<int:pk>/', views.FiscalCountry_detail, name='FiscalCountry_detail'),
    path('industry/', views.Industry_list, name='Industry_list'),
    path('industry/<int:pk>/', views.Industry_detail, name='Industry_detail'),
    path('segment/', views.Segment_list, name='Segment_list'),
    path('segment/<int:pk>/', views.Segment_detail, name='Segment_detail'),
    path('currencyrepository/', views.CurrencyRepository_list, name='CurrencyRepository_list'),
    path('currencyrepository/<int:pk>/', views.CurrencyRepository_detail, name='CurrencyRepository_detail'),
    path('exchangeratelibrary/', views.ExchangeRateLibrary_list, name='ExchangeRateLibrary_list'),
    path('exchangeratelibrary/<int:pk>/', views.ExchangeRateLibrary_detail, name='ExchangeRateLibrary_detail'),
    path('exchangeratelibrary_has_currentrepository/', views.ExchangeRateLibrary_has_CurrentRepository_list, name='ExchangeRateLibrary_has_CurrentRepository_list'),
    path('exchangeratelibrary_has_currentrepository/<int:pk>/', views.ExchangeRateLibrary_has_CurrentRepository_detail, name='ExchangeRateLibrary_has_CurrentRepository_detail'),
    path('project/', views.Project_list, name='Project_list'),
    path('project/<int:pk>/', views.Project_detail, name='Project_detail'),
    path('productType/', views.ProductType_list, name='ProductType_list'),
    path('productType/<int:pk>/', views.ProductType_detail, name='ProductType_detail'),
    path('product/', views.Product_list, name='Product_list'),
    path('product/<int:pk>/', views.Product_detail, name='Product_detail'),
    path('revenueScenario/', views.RevenueScenario_list, name='RevenueScenario_list'),
    path('revenueScenario/<int:pk>/', views.RevenueScenario_detail, name='RevenueScenario_detail'),
    path('revenueScenario_has_product/', views.RevenueScenarioHasProduct_list, name='RevenueScenarioHasProduct_list'),
    path('revenueScenarioHasproduct/<int:pk>/', views.RevenueScenarioHasProduct_detail, name='RevenueScenario_has_Product_detail'),

]

# Html hyperlinks to the API endpoints
"""
 
    <a href="region/">Region</a>
    <a href="fiscalcountry/">FiscalCountry</a>
    <a href="industry/">Industry</a>
    <a href="segment/">Segment</a>
    <a href="currencyrepository/">CurrencyRepository</a>
    <a href="exchangeratelibrary/">ExchangeRateLibrary</a>
    <a href="exchangeratelibrary_has_currentrepository/">ExchangeRateLibrary_has_CurrentRepository</a>
    <a href="project/">Project</a>
    <a href="productType/">ProductType</a>
    <a href="product/">Product</a>
    <a href="revenueScenario/">RevenueScenario</a>
    <a href="revenueScenario_has_product/">RevenueScenario_has_Product</a>

"""