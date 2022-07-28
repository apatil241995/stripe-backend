from django.urls import path, include
from .views import checkout_session, Get_ProductDetails

urlpatterns = [
    path('checkout', checkout_session.as_view()),
    path('ProductDetails', Get_ProductDetails.as_view())
]