# Generated by Django 4.1.3 on 2022-11-24 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0003_alter_fiscalcountry_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='revenue.project'),
            preserve_default=False,
        ),
    ]
