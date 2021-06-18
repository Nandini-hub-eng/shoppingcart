from django.db import connections
from django.db import models

class productmodel(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.CharField(max_length=100)
    productquantity = models.CharField(max_length=100)
    productimage = models.CharField(max_length=100)
    displayorder = models.CharField(max_length=10)
    status = models.IntegerField(max_length=1)

    class Meta:
        db_table = "product"