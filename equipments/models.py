from django.db import models
from datetime import datetime

from consultants.models import Consultant

# Create your models here.
class Equipment(models.Model):
	consultant = models.ForeignKey(Consultant, on_delete=models.DO_NOTHING)
	equipment_name = models.CharField(max_length=200)
	equipment_type = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	quantity = models.IntegerField(default=0)
	description = models.TextField(blank=True)
	price = models.IntegerField()
	capacity = models.IntegerField()
	driver = models.IntegerField()
	sqft = models.IntegerField()
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
	photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	is_published = models.BooleanField(default=True)
	date_added = models.DateTimeField(default=datetime.now(), blank=True)
	def __str__(self):
		return self.equipment_name
