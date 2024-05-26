# jadwal_app/models.py
from django.db import models

class Guru(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nama

class MataPelajaran(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Jadwal(models.Model):
    hari = models.CharField(max_length=20)
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hari} {self.waktu_mulai} - {self.waktu_selesai}"
