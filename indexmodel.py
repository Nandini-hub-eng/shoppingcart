from django.db import connections
from django.db import models

class indexmodel(models.Model):
    categoryname = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"