# Generated by Django 4.2 on 2023-05-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0009_remove_batch_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='uuid',
            field=models.UUIDField(default='ae55a9f1-90ba-46cd-9332-9fb5fe52591c'),
        ),
    ]
