from django.db import models

# Create your models here.
class MoodEntry(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.IntegerField(auto_now_add=True)
    description = models.TextField()