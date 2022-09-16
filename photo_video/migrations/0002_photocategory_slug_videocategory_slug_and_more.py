# Generated by Django 4.0.6 on 2022-09-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photocategory',
            name='slug',
            field=models.SlugField(default='dfdsfd', unique=True),
        ),
        migrations.AddField(
            model_name='videocategory',
            name='slug',
            field=models.SlugField(default='fff', unique=True),
        ),
        migrations.AlterField(
            model_name='photocategory',
            name='cover',
            field=models.ImageField(upload_to='photo_library/covers', verbose_name='Изображение обложки'),
        ),
    ]