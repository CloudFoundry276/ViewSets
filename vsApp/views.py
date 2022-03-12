import imp
from django.shortcuts import render
from vsApp.models import Student
from vsApp.serializers import StudentSerializer
from rest_framework import viewsets


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
