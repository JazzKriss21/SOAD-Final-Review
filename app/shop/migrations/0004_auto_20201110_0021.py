# Generated by Django 3.0.3 on 2020-11-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Electronics'), (2, 'Apparels'), (3, 'Bags'), (4, 'Miscellaneous'), (5, 'All')], default=5),
        ),
    ]
