from django.db import models

# Create your models here.
class Order(models.Model):
	status = models.IntegerField()

class Product(models.Model):
	name = models.CharField(max_length = 128)
	price = models.IntegerField()
	orderproducts = models.ManyToManyField(Order, through = "OrderProduct")

class OrderProduct(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()