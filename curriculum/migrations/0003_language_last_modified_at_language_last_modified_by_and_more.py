# Generated by Django 4.2 on 2023-05-01 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum', '0002_alter_question_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='last_modified_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='uuid',
            field=models.UUIDField(default='471abd59-ad9b-427a-b1cc-2c65fbd3dbca'),
        ),
    ]