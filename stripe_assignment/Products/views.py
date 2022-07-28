from django.shortcuts import redirect
from rest_framework import generics
import stripe
from rest_framework.response import Response

from .serializer import productSerializer
from .models import ProductDetails

stripe.api_key = "sk_test_51LPJRsSAn1Qvta0uOxy4oY8CDknwNVVBldIz1Aip0YofsfCcOzaOFNEI6a7dgcFsBW0teraQPmpRbUkBH34FBx1E00wiyjKJ6c"


class checkout_session(generics.RetrieveAPIView):
    serializer_class = productSerializer

    def get(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LPkTlSAn1Qvta0u9SgsmkoW',
                    'quantity': 3,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000',
            cancel_url='http://127.0.0.1:8000'
        )
        return redirect(checkout_session.url, code=303)


class Get_ProductDetails(generics.RetrieveAPIView):
    serializer_class = productSerializer

    def get(self, request, **kwargs):
        data = ProductDetails.objects.all()
        serialized_data = productSerializer(data, many=True)
        return Response(data=serialized_data.data)
