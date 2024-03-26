from django.db import models


class Create(models.Model):
    choice = [('male', 'MALE'), ('female', 'FEMALE')]
    customer_name = models.CharField(max_length=20)
    mobile_no = models.IntegerField()
    gender = models.CharField(max_length=20, choices=choice)
    product_name = models.CharField(max_length=20)
    product_quantity = models.IntegerField()
    purchase_date = models.DateField()



