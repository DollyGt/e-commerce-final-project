# Generated by Django 2.0.6 on 2018-07-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
