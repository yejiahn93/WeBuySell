# Generated by Django 3.1.6 on 2021-04-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webuysell_app', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]