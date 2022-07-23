from django.urls import path
from .views import *

urlpatterns = [
    path("",AddEmployee.as_view(),name="add_employee"),
    path("employe_list/",EmployeeList.as_view(),name="employee_list"),
    path("employe/<int:id>",EmployeeDetail.as_view(),name="employee_detail"),
    path("task/",AddTask.as_view(),name="add_task"),
    path("task_list/",Tasks.as_view(),name="task_list"),
    path("task_detail/<int:id>",TaskDetail.as_view(),name="task_list")
    
]
