from django.contrib import admin

from .models import ProductImage, Product, Comment, Rating, RegistrationModel

# Register your models here.
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(RegistrationModel)

