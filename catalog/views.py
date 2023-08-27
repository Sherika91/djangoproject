from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Catalog'
        return context

    def get_queryset(self):
        return Product.objects.filter(in_stock=True)


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

    context = {
        'title': 'Contacts Us',
    }

    return render(requests, 'catalog/contacts.html', context)


def products(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'title': ' Our Products',
    }

    return render(request, 'catalog/products.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Product Details'
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price', 'in_stock']
    success_url = reverse_lazy('catalog:index')
