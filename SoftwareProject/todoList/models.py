from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.email

class Board(models.Model):
    board_name = models.CharField(max_length=30, null=True)
    users = models.ManyToManyField('User')

    def __str__(self):
        return self.board_name

task_statuses = [("TD", "To Do"),("IP", "In Progress"), ("D", "Done")]

class Task(models.Model):
    task_name = models.CharField(max_length=30, null=True)
    task_status = models.CharField(choices=task_statuses, max_length=2, null=True)
    task_back = models.BooleanField(default=True, null=True)
    user = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    board = models.ForeignKey('Board', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.task_name + ' ' + str(self.task_status)




