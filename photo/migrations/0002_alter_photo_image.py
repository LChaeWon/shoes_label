# Generated by Django 4.0.3 on 2022-05-10 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='shoes_data/%Y/%m/%d'),
        ),
    ]
