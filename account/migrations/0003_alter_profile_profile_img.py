# Generated by Django 4.2 on 2023-05-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_bio_alter_profile_profile_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(upload_to='profile_img/'),
        ),
    ]
