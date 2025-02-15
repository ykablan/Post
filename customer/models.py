from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=200, verbose_name="Müşteri Adı")

    def __str__(self):
        return self.customer_name
    
