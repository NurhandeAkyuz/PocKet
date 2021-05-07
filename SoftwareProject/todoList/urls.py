from django.contrib import admin
from django.urls import path
from . import views
from . import sessions

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('home/', views.homepage, name='homepage'),
    path('login/', sessions.session, name='login'),
    path('signup/', sessions.register, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('deleteboard/<board_id>', views.deleteboard, name='deleteboard'),
    path('editboard/<board_id>/delete/<int:task_id>', views.deletetask, name='deletetask'),
    path('editboard/<board_id>/todo/<int:task_id>', views.to_do, name='to_do'),
    path('editboard/<board_id>/doing/<int:task_id>', views.doing, name='doing'),
    path('editboard/<board_id>/createtask', views.createTask, name='createTask'),
    path('editboard/<board_id>/done/<int:task_id>', views.done, name='done'),
    path('editboard/<board_id>', views.editboard, name='editboard'),
    path('home/teammember/<int:user_id>', views.joinProject, name='joinProject'),
]