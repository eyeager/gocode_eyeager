from django.db import models

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()

class Dogs(models.Model):
	breed = models.CharField(max_length=120)
	name = models.CharField(max_length=20)