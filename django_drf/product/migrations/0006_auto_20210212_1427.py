# Generated by Django 3.1.6 on 2021-02-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]