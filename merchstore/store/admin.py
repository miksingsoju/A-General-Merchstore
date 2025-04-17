from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import *



class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType

class ProductImageInline(admin.TabularInline): 
    model = ProductImage
    extra = 1
    fields = ('image', 'description') 


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name','price','stock', 'status','profile_image')
    inlines = [ProductImageInline] 
         
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductType,ProductTypeAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
