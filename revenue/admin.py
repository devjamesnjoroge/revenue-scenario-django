from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Region)
admin.site.register(FiscalCountry)
admin.site.register(Industry)
admin.site.register(Segment)
admin.site.register(CurrencyRepository)
admin.site.register(ExchangeRateLibrary)
admin.site.register(ExchangeRateLibrary_has_CurrentRepository)
admin.site.register(Project)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(RevenueScenario)
admin.site.register(RevenueScenarioHasProduct)