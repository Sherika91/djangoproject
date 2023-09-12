from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Catalog'
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser or user.is_staff:
                queryset = Product.objects.all()
            else:
                queryset = super().get_queryset().filter(
                    in_stock=True
                )
        else:
            queryset = super().get_queryset().filter(
                in_stock=False
            )

        return queryset


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
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_staff:
            product_list = Product.objects.all()
        else:
            product_list = Product.objects.filter(in_stock=False)
    else:
        product_list = Product.objects.none()  # Return an empty queryset for anonymous users

    context = {
        'product_list': product_list,
        'title': 'Our Products',
    }

    return render(request, 'catalog/products.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Product Details'
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""

        context_data = super().get_context_data(**kwargs)

        version_form_set = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = version_form_set(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_form_set(instance=self.object)

        return context_data

    def form_valid(self, form):
        """Called if all forms are valid.
         Creates a Version instance along with the main Product instance."""

        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


def toggle_activity(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.in_stock:
        product.in_stock = False
    else:
        product.in_stock = True

    product.save()

    return redirect(reverse('catalog:index'))

