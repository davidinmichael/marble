# Generated by Django 4.2 on 2023-05-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_bio_profile_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='images/default.jpg', upload_to='profile_img/'),
        ),
    ]