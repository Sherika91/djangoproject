# Generated by Django 4.2.4 on 2023-08-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=100, verbose_name='Category'),
        ),
    ]
