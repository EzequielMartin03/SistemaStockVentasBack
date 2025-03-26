from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    dni_cuit = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
