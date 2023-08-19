from django.urls import path
from catalog.views import index, contacts, products, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('products/<int:id>/', product_detail, name='product_detail'),
]
