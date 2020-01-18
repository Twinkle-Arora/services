from .models import shop
from rest_framework import serializers

class shopSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = shop
        fields = ('spname', 'spownm', 'mob', 'location')


