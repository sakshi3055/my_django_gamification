# Generated by Django 5.0.6 on 2024-05-12 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.lessoncategory'),
        ),
    ]
