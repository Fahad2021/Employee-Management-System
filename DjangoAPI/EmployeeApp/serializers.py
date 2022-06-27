from dataclasses import field
from rest_framework import serializers
from EmployeeApp.models import Department,Employee

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('DepartmentId','DepartmentName')
    
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('EmployeeId',
        'EmployeeName',
        'Department',
        'DateofJoining',
        'photoFileName')
 