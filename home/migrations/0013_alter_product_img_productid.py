# Generated by Django 3.2.7 on 2021-11-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_product_color_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_img',
            name='productID',
            field=models.CharField(max_length=32),
        ),
    ]