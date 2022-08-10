from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class ProductDetails(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    images = ArrayField(ArrayField(models.URLField()))


    def __str__(self):
        return self.name


class PaymentDetail(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    amount_paid = models.IntegerField()
    payment_mode = models.CharField(max_length=200, blank=False, null=False)
    order_time = models.DateTimeField(default=timezone.now, blank=True)
