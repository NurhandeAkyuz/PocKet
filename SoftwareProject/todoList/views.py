from django.shortcuts import render, redirect
from .models import User, Board, Task
from .forms import BoardForm,  TaskForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html', {})

def homepage(request):
    if request.method == "POST":
        form = BoardForm(request.POST or None)
        if form.is_valid():
            form.save()
            email = request.session["email"]
            user = User.objects.get(email=email)
            b = Board.objects.get(board_name=form.cleaned_data["board_name"])
            b.users.add(user)
            b.save()
            messages.success(request, ('Project has been created!'))
            return redirect("homepage")
    else:
        email=request.session["email"]
        user = User.objects.get(email=email)
        user_boards=[]
        for p in Board.objects.all():
            if user in p.users.all():
                user_boards.append(p)
        return render(request, 'homepage.html', {'all_boards': user_boards})

def createTask(request, board_id):
    if request.method == "POST":
        board = Board.objects.get(pk=board_id)
        form = TaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data["task_name"]
            task = Task(task_name=task_name, board=board)
            task.save()
            messages.success(request, ('Task has been created!'))
    return redirect(reverse("editboard", kwargs={"board_id": board_id}))


def logout(request):
    return render(request, 'logout.html', {})

def deleteboard(request, board_id):
    board = Board.objects.get(pk=board_id)
    board.delete()
    messages.success(request, ('Project has been deleted!'))
    return redirect('homepage')

def deletetask(request, task_id, board_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Task has been deleted!'))
    return redirect(reverse("editboard", kwargs={"board_id": board_id}))


def to_do(request, task_id,board_id):
    board = Board.objects.get(pk=board_id)
    task = Task.objects.get(pk=task_id)
    task.task_status = "TD"
    task.save()
    return redirect(reverse("editboard", kwargs={"board_id": board_id}))

def doing(request, board_id, task_id):
    task = Task.objects.get(pk=task_id)
    task.task_status = "IP"
    task.save()
    return redirect(reverse("editboard", kwargs={"board_id": board_id}))

def done(request, task_id,board_id):
    board = Board.objects.get(pk=board_id)
    task = Task.objects.get(pk=task_id)
    task.task_status = "D"
    task.save()
    return redirect(reverse("editboard", kwargs={"board_id": board_id}))

def editboard(request, board_id):
    if request.method == "POST":
        board = Board.objects.get(pk=board_id)
        form = BoardForm(request.POST or None, instance=board)
        if form.is_valid():
            form.save()
            messages.success(request, ('Project has been edited!'))
            return redirect('homepage')
    else:
        board = Board.objects.get(pk=board_id)
        return render(request, 'editboard.html', {'board': board})

def joinProject(request,user_id):
    if request.method == "POST":
        user = User.objects.get(pk=user_id)
        form = BoardForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            email = request.session["email"]
            user = User.objects.get(email=email)
            b = Board.objects.get(board_name=form.cleaned_data["board_name"])
            b.users.add(user)
            b.save()
            messages.success(request, ('Member has been added!'))
    return redirect(reverse("joinProject", kwargs={"user_id": user_id}))

