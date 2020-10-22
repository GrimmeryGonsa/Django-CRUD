from django.urls import path,include
from . import views

urlpatterns = [
    path('employee/form',views.employee_form,name='employee_insert'),#get and post request for insert operation
    path('employee/list/',views.employee_list,name='employee_list'),#get and post request for update operation
    path('employee/<int:id>/',views.employee_form,name='employee_update'),#get request to retrive and dislay all records
    path('employee/delete/<int:id>/',views.employee_delete,name="employee_delete" ),
    path('',views.index,name='index'),

    
]
