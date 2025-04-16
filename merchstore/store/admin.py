from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name','price','stock', 'status')

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductType,ProductTypeAdmin)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
