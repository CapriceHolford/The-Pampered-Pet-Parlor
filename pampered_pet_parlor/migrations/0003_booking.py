# Generated by Django 4.2.17 on 2025-01-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pampered_pet_parlor', '0002_blogpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('service', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]