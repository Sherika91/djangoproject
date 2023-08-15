from django.shortcuts import render
from catalog.models import Product


def index(requests):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list
      }
    return render(requests, 'catalog/index.html', context)


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        print(f"{name}, ({email}) says: {subject}\n{message}")
    return render(requests, 'catalog/contacts.html')
