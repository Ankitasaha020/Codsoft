# Generated by Django 4.0.3 on 2022-05-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_total_stocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_stocks',
            field=models.IntegerField(),
        ),
    ]
