# Generated by Django 3.0 on 2019-12-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0007_auto_20191210_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_back',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
