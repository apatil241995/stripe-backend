from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import generics
import stripe
from rest_framework.response import Response

from .serializer import productSerializer, paymentSerializer
from .models import ProductDetails

stripe.api_key = "sk_test_51LPJRsSAn1Qvta0uOxy4oY8CDknwNVVBldIz1Aip0YofsfCcOzaOFNEI6a7dgcFsBW0teraQPmpRbUkBH34FBx1E00wiyjKJ6c"
endpoint_secret = 'whsec_c91dce48d5dc9f273ce2480eb634cb5888b77509a5c82928f04753d95ef4a62b'


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
            success_url='http://localhost:3000' + '?success=true',
            cancel_url='http://localhost:3000'
        )
        return redirect(checkout_session.url, code=303)


class Get_ProductDetails(generics.RetrieveAPIView):
    serializer_class = productSerializer

    def get(self, request, **kwargs):
        data = ProductDetails.objects.all()
        serialized_data = productSerializer(data, many=True)
        return Response(data=serialized_data.data)


class PostPaymentData(generics.CreateAPIView):
    serializer_class = paymentSerializer

    def post(self, request, *args, **kwargs):
        payload = request.body
        header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, header, endpoint_secret
            )
        except ValueError as e:
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            return HttpResponse(status=400)

        # this will handle the completed checkout session
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']

            customer_name = session["customer_details"]["name"]
            customer_email = session["customer_details"]["email"]
            amount_total = session["amount_total"]
            payment_method = session["payment_method_types"][0]
            data = {
                "name": customer_name,
                "email": customer_email,
                "amount_paid": amount_total/100,
                "payment_mode": payment_method
            }
            serialized_data = paymentSerializer(data=data)
            if serialized_data.is_valid():
                serialized_data.save()

        return HttpResponse(status=200)
