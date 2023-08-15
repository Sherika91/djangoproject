from django.contrib import admin
from catalog.models import Product, Category

# My registered models
# admin.site.register(Category)
# admin.site.register(Product)


# My registered models with custom settings
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description',)
    search_fields = ('category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'in_stock')
    search_fields = ('name', 'category',)
    list_filter = ('name', 'category', 'price', 'in_stock',)
