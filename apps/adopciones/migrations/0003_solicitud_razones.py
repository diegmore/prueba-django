# Generated by Django 2.2.6 on 2019-11-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopciones', '0002_solicitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='razones',
            field=models.TextField(blank=True, null=True),
        ),
    ]
