from django.shortcuts import redirect
from rest_framework import generics
import stripe
from rest_framework.response import Response

from .serializer import productSerializer
from .models import ProductDetails

stripe.api_key = "sk_test_51LPJRsSAn1Qvta0uOxy4oY8CDknwNVVBldIz1Aip0YofsfCcOzaOFNEI6a7dgcFsBW0teraQPmpRbUkBH34FBx1E00wiyjKJ6c"


class checkout_session(generics.RetrieveAPIView):
    serializer_class = productSerializer

    def get(self, request, quantity, id):
        product = data = ProductDetails.objects.get(id=id)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': int(product.price * 100),
                        'product_data': {
                            'name': product.name,
                            'images': [product.image_1]
                        }
                    },
                    'quantity': quantity,
                }
            ],
            mode='payment',
            metadata={
                'product_id': product.id
            },
            success_url='http://localhost:3001' + '?success=true',
            cancel_url='http://localhost:3001'
        )
        return redirect(checkout_session.url, code=303)


class Get_ProductDetails(generics.RetrieveAPIView):
    serializer_class = productSerializer

    def get(self, request, **kwargs):
        data = ProductDetails.objects.all()
        serialized_data = productSerializer(data, many=True)
        return Response(data=serialized_data.data)
