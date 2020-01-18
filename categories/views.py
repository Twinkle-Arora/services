from categories.models import Catg, Type, Product
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import shop
from .serializers import shopSerializers
from rest_framework import viewsets, mixins
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point


def homepg(request):
    allc = Catg.objects.all()
    context = {
        'allc': allc
    }
    return render(request, 'hmpg.html', context)


def type1(request, Catg_id):
    ca = Catg.objects.get(pk=Catg_id)
    allt = Type.objects.all()
    context1 = {
        'allt': allt,
        'ca': ca,

    }
    return render(request, "type.html", context1)


def prod(request, Type_id, Catg_id):
    ca = Catg.objects.get(pk=Catg_id)
    p = Type.objects.get(pk=Type_id)
    allp = Product.objects.all()
    context2 = {
        'p': p,
        'allp': allp,
        'ca': ca,

    }
    return render(request, "product.html", context2)


# def ch(request, Type_id, Product_id, Catg_id):
#     ca = Catg.objects.get(pk=Catg_id)
#     p = Type.objects.get(pk=Type_id)
#     cho = Product.objects.get(pk=Product_id)
#     alls = Choice.objects.all()
#     context3 = {
#         'p': p,
#         'alls': alls,
#         'cho': cho,
#         'ca': ca,
#     }
#     return render(request, "listofsp.html", context3)

# class shoplist(viewsets.ModelViewSet):
#     # def get(self):
#     queryset = shop.objects.all()
#     serializer_class = shopSerializers
#     # return Response(serializer.data)
#

q = "jabalpur"


def words_to_point(q):
    geolocator = Nominatim()
    location = geolocator.geocode(q)
    point = Point(location.longitude, location.latitude)
    return point


# class LocationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """ Searchable list of locations
#
#     GET params:
#
#     - q - Location search paramater (New York or 10001)
#     - distance - Distance away. Defaults to 50
#     """
#     serializer_class = shopSerializers
#     queryset = shop.objects.all()
#
#     def get_queryset(self, *args, **kwargs):
#         queryset = self.queryset
#         q = self.request.GET.get('q')
#         distance = self.request.GET.get('distance', 50)
#         if q:
#             point = words_to_point(q)
#             distance = D(mi=distance)
#             queryset = queryset.filter(point__distance_lte=(point, distance))
#         return queryset

class shoplist(viewsets.ModelViewSet):
    queryset = shop.objects.all()
    serializer_class = shopSerializers


# def Chatc(request, Type_id, Product_id, Catg_id, Choice_id):
#     ca = Catg.objects.get(pk=Catg_id)
#     p = Type.objects.get(pk=Type_id)
#     cho = Product.objects.get(pk=Product_id)
#     cha = Product.objects.get(pk=Choice_id)
#     allc = Chat.objects.all()
#     context4 = {
#         'p': p,
#         'allc': allc,
#         'cho': cho,
#         'ca': ca,
#         'cha': cha,
#     }
#     return render(request, "listofsp.html", context4)
