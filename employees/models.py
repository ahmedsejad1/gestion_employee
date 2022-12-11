from django.db import models

# Create your models here.
class Service(models.Model):
    id_service=models.AutoField(primary_key=True)
    service=models.CharField(max_length=50)
    class Meta:
        db_table="service"

class Emloyees(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    class Meta:
        db_table="employee"
