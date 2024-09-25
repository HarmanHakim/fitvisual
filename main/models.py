import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TokoEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()
    description = models.TextField()
    