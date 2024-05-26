
from rest_framework import viewsets
from .models import Jadwal, Guru, MataPelajaran
from .serializers import JadwalSerializer, GuruSerializer, MataPelajaranSerializer

class GuruViewSet(viewsets.ModelViewSet):
    queryset = Guru.objects.all()
    serializer_class = GuruSerializer

class MataPelajaranViewSet(viewsets.ModelViewSet):
    queryset = MataPelajaran.objects.all()
    serializer_class = MataPelajaranSerializer

class JadwalViewSet(viewsets.ModelViewSet):
    queryset = Jadwal.objects.all()
    serializer_class = JadwalSerializer
