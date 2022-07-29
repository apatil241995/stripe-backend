from django.urls import path, include
from .views import checkout_session, Get_ProductDetails, PostPaymentData

urlpatterns = [
    path('checkout/<id>/<quantity>', checkout_session.as_view()),
    path('ProductDetails', Get_ProductDetails.as_view()),
    path('paymentdetails', PostPaymentData.as_view())
]