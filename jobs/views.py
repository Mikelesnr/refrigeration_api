from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'jobs/home.html')

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
