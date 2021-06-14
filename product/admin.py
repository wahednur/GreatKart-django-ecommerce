from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('product_name', 'price', 'discount_price',
                    'description', 'category', 'stock', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    ordering = ('-product_name', )

admin.site.register(Product, ProductAdmin)
