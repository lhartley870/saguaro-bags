# Generated by Django 3.2 on 2022-05-10 20:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_size_order_smallest_to_largest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='order_smallest_to_largest',
            field=models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
