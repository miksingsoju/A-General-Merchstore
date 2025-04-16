from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    displayName = models.CharField(max_length=63)
    emailAddress = models.EmailField()

    def __str__(self):
        return self.displayName

'''
Stuff you can add:
Dashboard for the User as a Seller:
- No. of Items Sold
- Items sold
- Most sold item ?

Dashboard for the User as a Buyer:
- Total Orders
- Amount Spent
- 
'''