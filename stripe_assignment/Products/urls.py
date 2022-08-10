from django.urls import path, include
from .views import Checkoutsession, Get_ProductDetails, PostPaymentData

urlpatterns = [
    path('checkout/<id>/<quantity>', Checkoutsession.as_view()),
    path('ProductDetails', Get_ProductDetails.as_view()),
    path('paymentdetails', PostPaymentData.as_view())
]