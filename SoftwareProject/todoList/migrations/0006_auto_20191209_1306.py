# Generated by Django 3.0 on 2019-12-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0005_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('TD', 'To Do'), ('IP', 'In Progress'), ('D', 'Done')], max_length=2, null=True),
        ),
    ]
