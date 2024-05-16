from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Task


###########################todo Home page TASK333333333333333333333333333333
#this is whow to load the data from the frontend
def todo_home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_date') #this is for umcompleted task
    #we want to fetch multiple data based on their condition if it was one data you should you use get
    
    #how can we make copleted task
    completed_task = Task.objects.filter(is_completed=True) #this is for completed task
    
    context = {
        'tasks': tasks,
        'completed_task': completed_task,
    }
    return render (request, "todo/home.html", context)

###########################ADD FUNCTION TASK333333333333333333333333333333
def add_task(request):
    task = request.POST['task']
    #to create data need provide all the field in the models or dataabse those 3 data will be auto generated
    Task.objects.create(task=task)
        #the task will be add to the todo_home page
    return redirect ('todo_home')

###########################MARK AS DONE FUNCTION TASK333333333333333333333333333333
#using primary or id we can fetch data or edit it
def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk) #thi function will fetch the data from database it exist or not return true or 404
    task.is_completed= True
    task.save()
 
    return redirect('todo_home', )

###########################MARK AS UNDONE FUNCTION TASK333333333333333333333333333333
def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk) #thi function will fetch the data from database it exist or not return true or 404
    task.is_completed= False
    task.save()
 
    return redirect('todo_home', )

###########################EDIT FUNCTION TASK333333333333333333333333333333
def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    #get request means refresh something to the saver
    #post request means updating or sending somenting  to the server
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task      #.task is models task
        get_task.save()
        return redirect('todo_home')
    else:   #this is for get request
        context= {
            'get_task': get_task,
        }
    #we need when the edit icon is clicked be redirect to a page where i can fill in order to edit the task
    return render(request, 'todo/edit.html', context)


###########################DELETE TASK333333333333333333333333333333
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk) #thi function will fetch the data from database it exist or not return true or 404
    task.delete()
    return redirect('todo_home')
 
    