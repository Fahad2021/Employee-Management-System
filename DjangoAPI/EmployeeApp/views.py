from datetime import date
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department,Employee
from EmployeeApp.serializers import DepartmentSerializers,EmployeeSerializers

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
        departments=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Delete Successfully",safe=False)
