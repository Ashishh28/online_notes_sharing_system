# Generated by Django 5.1.2 on 2025-04-09 16:05

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='notes_files/'),
        ),
        migrations.AddField(
            model_name='note',
            name='subject',
            field=models.CharField(default='General', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
