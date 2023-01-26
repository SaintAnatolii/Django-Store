from django.contrib import admin
from .models import ProductCategory, Product, Basket 

admin.site.register(ProductCategory)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    search_fields = ('name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity',)