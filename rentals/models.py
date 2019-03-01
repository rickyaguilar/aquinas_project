from django.db import models
from datetime import datetime

# Create your models here.
class Rental(models.Model):
	equipment = models.CharField(max_length=200)
	equipment_id = models.IntegerField(blank=True, null=True)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField(blank=True)
	status = models.CharField(max_length=100, blank=True)
	contact_date = models.DateTimeField(default=datetime.now(), blank=True)
	user_id = models.IntegerField(blank=True)
	def __str__(self):
		return self.name