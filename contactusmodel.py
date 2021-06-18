from django.db import connections
from django.db import models

class contactusmodel(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=10)

    class Meta:
        db_table = "contactus"