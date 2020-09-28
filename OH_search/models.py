from django.db import models

# Create your models here.

class Hydroxide(models.Model):
	Name = models.CharField(max_length=15)
	
	M = models.CharField(max_length=3)
	X1 = models.CharField(max_length=3)
	X2 = models.CharField(max_length=3)
	Energy = models.TextField()
	
	def __str__(self):
		return self.Name
