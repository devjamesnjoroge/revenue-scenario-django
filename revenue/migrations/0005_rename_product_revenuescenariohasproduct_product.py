# Generated by Django 4.1.3 on 2022-11-25 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0004_product_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenuescenariohasproduct',
            old_name='product',
            new_name='Product',
        ),
    ]
