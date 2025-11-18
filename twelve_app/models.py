from django.db import models

class Manufacturer(models.Model):
    name = models.CharField()
    foundation_date = models.DateField
    
class Item(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField()
    
class Publisher(models.Model):
    name = models.CharField()
    
class Book(models.Model):
    name = models.CharField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
