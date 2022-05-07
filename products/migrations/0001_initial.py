# Generated by Django 3.2 on 2022-05-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('friendly_name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
