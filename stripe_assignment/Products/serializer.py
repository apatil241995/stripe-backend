from rest_framework import serializers
from .models import ProductDetails, PaymentDetail


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = "__all__"


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = "__all__"
