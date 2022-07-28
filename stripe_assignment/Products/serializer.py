from rest_framework import serializers
from .models import ProductDetails


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = "__all__"
