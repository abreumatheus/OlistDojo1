# Generated by Django 3.1.6 on 2021-02-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20210212_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='product.Category'),
        ),
    ]