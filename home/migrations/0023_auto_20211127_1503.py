# Generated by Django 3.2.7 on 2021-11-27 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_order_productcapacity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_img',
            new_name='Product_img_color',
        ),
        migrations.DeleteModel(
            name='Product_color',
        ),
    ]
