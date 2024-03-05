from django.urls import path

from main.views import EmployeeList

urlpatterns = [
    path('employee-list', EmployeeList.as_view(), name='employee_list')
]
