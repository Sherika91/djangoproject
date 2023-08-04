from django.shortcuts import render


def index(requests):
    return render(requests, 'catalog/index.html')


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        print(f"{name}, ({email}) says: {subject}\n{message}")
    return render(requests, 'catalog/contacts.html')
