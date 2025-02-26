# Generated by Django 5.0.6 on 2024-06-28 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('availability', models.BooleanField()),
                ('contactInfo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('availability', models.BooleanField()),
                ('contactInfo', models.CharField(max_length=100)),
            ],
        ),
    ]
