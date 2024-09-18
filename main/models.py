import uuid
from django.db import models

# Create your models here.
class TokoEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()
    description = models.TextField()