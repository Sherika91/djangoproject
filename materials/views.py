from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from materials.models import Material
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, redirect


class MaterialCreateView(CreateView):
    model = Material
    fields = ['title', 'body']
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.title)
            new_material.save()

            return super().form_valid(form)


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ['title', 'body']
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.title)
            new_material.save()

            return super().form_valid(form)

    def get_success_url(self):
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')


class MaterialListView(ListView):
    model = Material

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset


class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


def toggle_activity(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if material.is_published:
        material.is_published = False
    else:
        material.is_published = True

    material.save()

    return redirect(reverse('materials:list'))
