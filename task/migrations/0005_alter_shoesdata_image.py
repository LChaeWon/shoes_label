# Generated by Django 4.0.3 on 2022-05-10 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_shoesdata_remove_photo_data_group_delete_datagroup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoesdata',
            name='image',
            field=models.ImageField(upload_to='data/'),
        ),
    ]