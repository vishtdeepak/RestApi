from django.db import models
from customoth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name =models.CharField(max_length=50)
    class Meta:
        db_table = "profile"