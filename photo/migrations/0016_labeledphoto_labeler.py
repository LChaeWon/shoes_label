# Generated by Django 4.0.3 on 2022-05-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0015_remove_photo_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='labeledphoto',
            name='labeler',
            field=models.CharField(default='tester', max_length=32),
            preserve_default=False,
        ),
    ]
