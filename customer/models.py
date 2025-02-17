from django.db import models
from django.urls import reverse


class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Müşteri Adı")
    address = models.TextField(verbose_name="Müşteri Adresi")
    phone=models.CharField(max_length=50, verbose_name="Müşteri Telefonu")
    checked = models.BooleanField(default=True, verbose_name="Aktif-Pasif")
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('customer:detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('customer:update', kwargs={'pk': self.pk})
    
    
    def get_delete_url(self):
        return reverse('customer:delete', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-created_date']
    
