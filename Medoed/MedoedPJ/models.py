from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    price = models.DecimalField( max_digits=7, decimal_places=2)
    photo = models.ImageField(upload_to='media', null=True)