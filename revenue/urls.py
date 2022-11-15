from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('get_regions', views.get_regions, name='get_regions'),
    path('post_region', views.post_region, name='post_region'),
    path('get_fiscal_countries', views.get_fiscal_countries, name='get_fiscal_countries'),
    path('post_fiscal_country', views.post_fiscal_country, name='post_fiscal_country'),
    path('get_industries', views.get_industries, name='get_industries'),
    path('post_industry', views.post_industry, name='post_industry'),
    path('get_segments', views.get_segments, name='get_segments'),
    path('post_segment', views.post_segment, name='post_segment'),
    path('get_currency_repositories', views.get_currency_repositories, name='get_currency_repositories'),
    path('post_currency_repository', views.post_currency_repository, name='post_currency_repository'),
    path('get_exchange_rate_library', views.get_exchange_rate_libraries, name='get_exchange_rate_libraries'),
    path('post_exchange_rate_library', views.post_exchange_rate_library, name='post_exchange_rate_library'),
    path('get_exchange_rate_has_current_repository', views.get_exchange_rate_has_current_repository, name='get_exchange_rate_has_current_repository'),
    path('post_exchange_rate_has_current_repository', views.post_exchange_rate_has_current_repository, name='post_exchange_rate_has_current_repository'),
    path('get_project', views.get_project, name='get_project'),
    path('post_project', views.post_project, name='post_project'),
    path('get_product', views.get_product, name='get_product'),
    path('post_product', views.post_product, name='post_product'),
    path('get_product_type', views.get_product_type, name='get_product_type'),
    path('post_product_type', views.post_product_type, name='post_product_type'),
    path('get_revenue_scenario', views.get_revenue_scenario, name='get_revenue_scenario'),
    path('post_revenue_scenario', views.post_revenue_scenario, name='post_revenue_scenario'),
    path('get_revenue_scenario_has_product', views.get_revenue_scenario_has_product, name='get_revenue_scenario_has_product'),
    path('post_revenue_scenario_has_product', views.post_revenue_scenario_has_product, name='post_revenue_scenario_has_product'),
    
]