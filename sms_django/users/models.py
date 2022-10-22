from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique=True, editable=False)
    phone = models.CharField(max_length=20)
    confirm = models.PositiveIntegerField(null=True, blank=True)
