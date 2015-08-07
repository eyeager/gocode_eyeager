from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class State(models.Model):
	status = models.CharField(max_length=15)

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	street_address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=30)
	zip_code = models.CharField(max_length=9)
	credit_card = models.CharField(max_length=16)

class Order(models.Model):
	status = models.ForeignKey(State)
	customer = models.ForeignKey(Customer)

class Product(models.Model):
	name = models.CharField(max_length = 128)
	description = models.TextField()
	price = models.FloatField()
	orderproducts = models.ManyToManyField(Order, through = "OrderProduct")

class OrderProduct(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	#tracking_number = models.CharField(max_length=100)