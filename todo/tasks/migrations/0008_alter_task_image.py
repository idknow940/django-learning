# Generated by Django 3.2.6 on 2021-08-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(default='/tasks/images/default.png', upload_to='task_images'),
        ),
    ]
