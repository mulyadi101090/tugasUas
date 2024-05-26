
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuruViewSet, MataPelajaranViewSet, JadwalViewSet

router = DefaultRouter()
router.register(r'guru', GuruViewSet)
router.register(r'mata_pelajaran', MataPelajaranViewSet)
router.register(r'jadwal', JadwalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
