# Generated by Django 3.1.2 on 2020-10-13 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('tourist_spots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.adress'),
        ),
    ]
