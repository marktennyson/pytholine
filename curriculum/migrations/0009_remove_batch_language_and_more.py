# Generated by Django 4.2 on 2023-05-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0008_studentanswer_score_alter_question_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='language',
        ),
        migrations.RemoveField(
            model_name='questioncategory',
            name='language',
        ),
        migrations.AlterField(
            model_name='question',
            name='uuid',
            field=models.UUIDField(default='278b3c6e-4531-48e9-a5ee-d8b2687e69c7'),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
