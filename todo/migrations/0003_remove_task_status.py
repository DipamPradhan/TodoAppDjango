# Generated by Django 5.1 on 2024-08-31 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
