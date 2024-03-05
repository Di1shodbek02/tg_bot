from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from main.models import Employee, Position
from main.serializer import EmployeeSerializer


class EmployeeList(GenericAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self, *args, **kwargs):
        return Employee.objects.all()

    def get(self, request, *args, **kwargs):
        employee = self.get_queryset()
        serializer = self.get_serializer(employee, many=True)
        employee_list = []
        for employee in serializer.data:
            employee['position'] = Position.objects.get(pk=employee['position']).name
            employee_list.append(employee)
        return Response(employee_list)
