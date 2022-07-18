from datetime import date
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department,Employee
from EmployeeApp.serializers import DepartmentSerializers,EmployeeSerializers
from django.core.files.storage import default_storage

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments=Department.objects.all()
        departments_serilizers=DepartmentSerializers(departments,many=True)
        return JsonResponse(departments_serilizers.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serilizer=DepartmentSerializers(data=department_data)
        if departments_serilizer.is_valid():
            departments_serilizer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to save",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serilizer=DepartmentSerializers(department, data=department_data)
        if departments_serilizer.is_valid():
            departments_serilizer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Falied to update",safe=False)

    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Delete Successfully",safe=False)
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees=Employee.objects.all()
        employees_serilalizer=EmployeeSerializers(employees,many=True)
        return JsonResponse(employees_serilalizer.data,safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serilalizer=EmployeeSerializers(data=employee_data)
        if employee_serilalizer.is_valid():
            employee_serilalizer.save()
            return JsonResponse("Add Employee successfully",safe=False)
        return JsonResponse("Failed to save employee",safe=False)

    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serilizer=EmployeeSerializers(employee, data=employee_data)
        if employees_serilizer.is_valid():
            employees_serilizer.save()
            return JsonResponse("Update successfully Employee",safe=False)
        return JsonResponse("Falied to update Employee",safe=False)
    elif request.method=='DELETE':
        employee=Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Delete sucessfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES["uploadedFile"]
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)