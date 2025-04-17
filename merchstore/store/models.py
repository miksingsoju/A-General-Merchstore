from django.db import models
from django.urls import reverse

from user_management.models import Profile

# Create your models here.

class ProductType(models.Model):
    name =  models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

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
    price = models.DecimalField(max_digits=99, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)
    profile_image = models.ImageField(upload_to='product_images', blank=True, null=True)

    class Status(models.TextChoices):
        AVAILABLE = 'Available'
        ON_SALE = 'On sale'
        OUT_OF_STOCK = 'Out of stock'

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id])

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/', null=False)
    description = models.TextField(max_length=255)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_image"
    )

class Transaction (models.Model):
    buyer = models.ForeignKey(
        Profile,
        on_delete = models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete = models.SET_NULL,
        null = True
    )
    # TODO: I might need to do something like add conditions?

    class Status(models.TextChoices):
        ON_CART = 'on cart','ON CART'
        TO_PAY = 'to pay', 'TO PAY'
        TO_SHIP = 'to ship', 'TO SHIP'
        TO_RECEIVE = 'to receive', 'TO RECEIVE'
        DELIVERED = 'delivered', 'DELIVERED' 

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
    )

    createdOn = models.DateTimeField(auto_now_add=True)

