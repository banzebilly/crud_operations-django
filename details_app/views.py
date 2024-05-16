from django.shortcuts import render, get_object_or_404
from .models import Employee



# Create your views here.
def home(request):
    
    emp = Employee.objects.all()
    context = {
        'emp': emp,
    }
    
    
    return render(request, 'home.html', context)


def emp_details(request, pk):
    single_emp = get_object_or_404(Employee, pk=pk)  # if you want to get one single data from databbase use get but if is multiple data use filter or all()
    
    context = {
        'single_emp': single_emp
    }
    return render (request, "details.html", context)