from django.db import models

class WarehouseAccess(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  