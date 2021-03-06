# Generated by Django 3.1.2 on 2020-11-02 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20201102_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='findsimilarmaterial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='findsimilarmaterial',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='materials',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materials',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
