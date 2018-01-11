from django.db import models

# Create your models here.
class user(models.Model):
    id=models.AutoField(primary_key=True)
    age=models.IntegerField(null=True)
    user_name=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
