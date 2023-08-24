from django.urls import path
from catalog.views import contacts, products, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
