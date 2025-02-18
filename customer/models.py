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
    
class Contact(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Müşteri", related_name="contacts")
    name=models.CharField(max_length=200, verbose_name="Kontak")
    title = models.CharField(max_length=200, verbose_name="Görevi")
    email = models.EmailField(verbose_name="email")
    phone =models.CharField(max_length=100, verbose_name="Telefon")

    def __str__(self):
        return self.name
    
    def get_delete_url(self):
        try:
            return reverse('customer:con_delete', kwargs={'pk': self.id})
        except :
            return ''
        
    def get_update_url(self):
        try:
            return reverse('customer:con_update', kwargs={'pk': self.id})
        except :
            return ''

    
    