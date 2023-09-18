from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Book(models.Model):
    status_book = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'Sold'),
    ]
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50,null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    rental_total_profit = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, default='Available', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title