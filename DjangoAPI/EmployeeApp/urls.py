
from django.urls import path, re_path
from EmployeeApp import views
from . import views

urlpatterns=[
    re_path(r'^department/$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi)
]