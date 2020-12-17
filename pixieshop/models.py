from django.db import models

# Create your models here.

class Product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=50)
    productDescription = models.CharField(max_length=300)
    pubDate = models.DateField()

    def __str__(self) -> str:
        return self.productName