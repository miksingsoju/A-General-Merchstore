from django.db import models
from django.urls import reverse


# Create your models here.

class ProductType(models.Model):
    name =  models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('store:productType-detail', args=[self.id])
    
    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=255)
    productType = models.ForeignKey(
        ProductType,
        on_delete = models.SET_NULL,
        null = True,
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)

    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        ON_SALE = 'on_sale', 'On sale'
        OUT_OF_STOCK = 'out_of_stock', 'Out of stock'

    # TODO: I might need to do something like add conditions?
    
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
    )
