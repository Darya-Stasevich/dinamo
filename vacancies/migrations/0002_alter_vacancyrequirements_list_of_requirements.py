# Generated by Django 4.0.6 on 2022-08-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancyrequirements',
            name='list_of_requirements',
            field=models.TextField(help_text='Скопируйте этот тег в Пункты требования: &lt;li&gt;ВВЕДИТЕ ВАШ ТЕКСТ В ЭТОМ ТЕГЕ&lt;/li&gt;', verbose_name='Пункты требования'),
        ),
    ]
