from rest_framework import serializers 
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model= Stock
       # fields=('ticker','volume') retuen only ticker and volume
        fields='__all__'