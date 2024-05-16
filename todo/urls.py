from django.urls import path
from . import views



urlpatterns = [
   
  
    
    path('', views.todo_home, name="todo_home"),
    #for the form to work and user can type their task and be addd to the database you need urls for that
    path('add_task/', views.add_task, name="add_task"),
    #in order to make a specific task as commpled or delete, you need a urls, by specifieng the id of the task you can do many operations
    path('mark_as_done/<int:pk>/', views.mark_as_done, name="mark_as_done"),
    #mark as undone task================================pk
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name="mark_as_undone"),
    #edit feature================edit the task when edit is click
    path('adit_task/<int:pk>/', views.edit_task, name="edit_task"),
    #delete task completely================when the delete icon is click
    path('delete_task/<int:pk>/', views.delete_task, name="delete_task"),
] 
