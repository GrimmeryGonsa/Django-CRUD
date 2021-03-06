from django.shortcuts import render,redirect
from .forms import EmployeeForm 
from .models import Employee


def index(request):
    return render(request,'employee_register/index.html')
# Create your views here.
def employee_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,'employee_register/employee_list.html',context)



def employee_form(request,id=0):
    
    if request.method=='POST':
        if id==0:
            form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    

    if id==0:
        form=EmployeeForm()
    else:
        employee=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=employee)
    

    context={
        "form":form,
    }
    




    
    return render(request,'employee_register/employee_form.html',context)


def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()


    return redirect('/employee/list')