# Generated by Django 3.2.6 on 2021-08-19 20:16

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_desc_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
