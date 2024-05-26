from rest_framework import serializers
from .models import Jadwal, Guru, MataPelajaran

class GuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guru
        fields = ['nama', 'email']

class MataPelajaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataPelajaran
        fields = ['nama', 'deskripsi']

class JadwalSerializer(serializers.ModelSerializer):
    guru = GuruSerializer()
    mata_pelajaran = MataPelajaranSerializer()

    class Meta:
        model = Jadwal
        fields = ['hari', 'waktu_mulai', 'waktu_selesai', 'guru', 'mata_pelajaran']

    def create(self, validated_data):
        guru_data = validated_data.pop('guru')
        mata_pelajaran_data = validated_data.pop('mata_pelajaran')
        
        guru = Guru.objects.create(**guru_data)
        mata_pelajaran = MataPelajaran.objects.create(**mata_pelajaran_data)
        
        jadwal = Jadwal.objects.create(guru=guru, mata_pelajaran=mata_pelajaran, **validated_data)
        return jadwal
