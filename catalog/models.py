from django.db import models

NULL_BLANK = {'null': True, 'blank': True}


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Category',)
    description = models.TextField(verbose_name='Description', **NULL_BLANK,)

    def __str__(self):
        return f"{self.category} {self.description}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('category', 'description',)


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Product Name')
    description = models.TextField(verbose_name='Description', **NULL_BLANK,)
    image = models.ImageField(upload_to='products/', verbose_name='Image Preview', **NULL_BLANK, )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category',)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', **NULL_BLANK,)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created',)
    date_last_updated = models.DateTimeField(auto_now=True, verbose_name='Date Last Updated',)

    in_stock = models.BooleanField(default=True, verbose_name='In Stock',)

    def __str__(self):
        return f"{self.name} {self.category} {self.price} {self.date_created}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name', 'category', 'price', 'date_created', 'in_stock',)


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Subject Name',)
    description = models.TextField(verbose_name='Description', **NULL_BLANK,)

    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product',)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Product',)
    version_name = models.CharField(max_length=100, verbose_name='Version Name',)
    version_number = models.CharField(max_length=10, verbose_name='Version Number',)
    is_active = models.BooleanField(default=True, verbose_name='Is Active',)

    def __str__(self):
        return f'{self.product} - Version {self.version_number}'

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'
        ordering = ('product', 'version_name', 'version_number',  'is_active',)
