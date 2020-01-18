from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Catg, Type, Product, shop

class shopAdmin(LeafletGeoAdmin):
     pass

admin.site.register(Catg)
admin.site.register(Type)
admin.site.register(Product)
# admin.site.register(Choice)
admin.site.register(shop, shopAdmin)
# admin.site.register(Chat)




