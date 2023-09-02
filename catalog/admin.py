from django.contrib import admin
from catalog.models import Product, Category, Subject, Version


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
    list_display = ('id', 'name', 'category', 'price', 'in_stock',)
    search_fields = ('name', 'category',)
    list_filter = ('name', 'category', 'price', 'in_stock',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product',)
    search_fields = ('name', 'product',)
    list_filter = ('product',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_name', 'version_number', 'is_active',)
    search_fields = ('product',  'version_name', 'version_number',)
    list_filter = ('product', 'version_name', 'version_number', 'is_active',)
