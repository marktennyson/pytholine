# Generated by Django 4.2 on 2023-05-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0005_language_logo_url_alter_question_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='language',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='uuid',
            field=models.UUIDField(default='7edce7fe-4c04-46fb-9ab9-332bcc977c73'),
        ),
    ]