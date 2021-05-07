# Generated by Django 3.0 on 2019-12-09 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0002_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='users',
            field=models.ManyToManyField(to='todoList.User'),
        ),
        migrations.AddField(
            model_name='task',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todoList.Board'),
        ),
    ]
