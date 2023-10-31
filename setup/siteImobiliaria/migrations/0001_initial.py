# Generated by Django 4.2.6 on 2023-10-31 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imoveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('status', models.TextField()),
                ('area', models.TextField()),
                ('bedrooms', models.TextField()),
                ('bathrooms', models.TextField()),
                ('floor', models.TextField()),
                ('parking', models.TextField()),
                ('value', models.TextField()),
                ('type', models.TextField()),
                ('path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('subject', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]