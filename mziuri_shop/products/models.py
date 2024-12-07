from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField(default="")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    create_date=models.DateField(auto_now_add=True)
    write_time=models.DateTimeField(auto_now=True)
    views=models.PositiveIntegerField()