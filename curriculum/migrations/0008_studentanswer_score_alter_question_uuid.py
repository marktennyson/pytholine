# Generated by Django 4.2 on 2023-05-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0007_alter_question_last_modified_by_alter_question_uuid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='question',
            name='uuid',
            field=models.UUIDField(default='81b2c525-559c-4c19-ab15-9a4f99494cc5'),
        ),
    ]
