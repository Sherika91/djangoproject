from django.shortcuts import render
from catalog.models import Product


def index(requests):
    product_list = Product.objects.all()[:3]
    context = {
        'product_list': product_list,
        'title': 'Catalog',
      }
    return render(requests, 'catalog/index.html', context)


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


# def chosen_product(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {
#         'product_list': Product.objects.filter(category_id=pk),
#         'title': f'{product}',
#     }
#
#     return render(request, 'catalog/includes/inc_all_products.html', context)
