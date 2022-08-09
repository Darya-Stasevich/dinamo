# Generated by Django 4.0.6 on 2022-08-09 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_attachment_alter_service_title_service_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='attachment',
            field=models.ForeignKey(blank=True, help_text='Если нужно прикрепить доп.информацию по услуге', null=True, on_delete=django.db.models.deletion.CASCADE, to='services.attachment', verbose_name='Прикрепленный файл'),
        ),
    ]