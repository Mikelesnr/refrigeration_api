from rest_framework import viewsets
from .models import Technician
from .serializers import TechnicianSerializer

class TechnicianViewSet(viewsets.ModelViewSet):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
