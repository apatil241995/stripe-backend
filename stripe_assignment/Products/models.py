from django.db import models


class ProductDetails(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image_1 = models.URLField()
    image_2 = models.URLField()
    image_3 = models.URLField()
    image_4 = models.URLField()

    def __str__(self):
        return self.name


class PaymentDetails(models.Model):
    price = models.CharField(max_length=100)
