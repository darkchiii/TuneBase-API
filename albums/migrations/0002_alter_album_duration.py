# Generated by Django 5.0.1 on 2024-09-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]
