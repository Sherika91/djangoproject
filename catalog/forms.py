from django import forms

from catalog.models import Product, Version

forbidden_words_to_filter = ['казино' 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleForMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'description', 'category', 'price', 'image', 'in_stock']
        exclude = ['created_at', 'updated_at']

    def clean_name(self):

        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        for word in forbidden_words_to_filter:
            if word in cleaned_data:
                raise forms.ValidationError(f'Word {word} is not allowed in name')

        return cleaned_data

    def clean_description(self):

        cleaned_data = self.cleaned_data['description']
        for word in forbidden_words_to_filter:
            if word in cleaned_data:
                raise forms.ValidationError(f'Word {word} is not allowed in description')

        return cleaned_data


class VersionForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_name', 'version_number', 'is_active',)
