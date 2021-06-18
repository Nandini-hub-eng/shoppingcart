from django.db import connections
from django.db import models

class cartmodel(models.Model):
    userid = models.IntegerField(max_length=10)
    productid = models.IntegerField(max_length=10)
    qty = models.IntegerField(max_length=10)

    class Meta:
        db_table = "cart"