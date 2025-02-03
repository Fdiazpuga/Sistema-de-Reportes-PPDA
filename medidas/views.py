from rest_framework import viewsets
from .models import Medida, Actividad
from .serializers import MedidaSerializer, ActividadSerializer

class MedidaViewSet(viewsets.ModelViewSet):
    queryset = Medida.objects.all()
    serializer_class = MedidaSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
