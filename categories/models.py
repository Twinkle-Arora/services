from django.db.models import Manager as GeoManager
from django.db import models
from django.contrib.gis.db import models
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point



# Create your models here.
class Catg(models.Model):
    name = models.CharField(max_length=100)
    img = models.FileField(upload_to='categories/media/images/')


    def __str__(self):
        return self.name + " " + str(self.img)



class Type(models.Model):
    tname = models.ForeignKey(Catg, on_delete=models.CASCADE)
    cn = models.CharField(max_length=100, default=" ")
    image = models.FileField(upload_to='categories/media/images/')


    def __str__(self):
        return self.cn + " " + str(self.image)

class Product(models.Model):
    pname = models.ForeignKey(Type, on_delete=models.CASCADE)
    pn = models.CharField(max_length=100, default=" ")
    img = models.FileField(upload_to='categories/media/images/')

    def __str__(self):
        return self.pn + " " + str(self.img)

# class Choice(models.Model):
#     chname = models.ForeignKey(Product, on_delete=models.CASCADE)
#     chn = models.CharField(max_length=1000, default=" ")
#
#
#     def __str__(self):
#         return self.chn

class shop(models.Model):
    spname = models.CharField(max_length=150, default=" ")
    spownm = models.CharField(max_length=100, default=" ")
    mob = models.BigIntegerField(blank=False, null=False, unique=True)
    city = models.CharField(max_length=255)
    location = models.PointField(srid=4326)
    objects = GeoManager()






