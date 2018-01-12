from __future__ import unicode_literals
# Create your models here.
from django.db import models



class UserData(models.Model):
	name=models.CharField(max_length=150)
	surname=models.CharField(max_length=150)
	field_choice =[
			('website', 'WebSite'),
    		('Photography', 'Wedding Photography'),
    		('Photography', 'Pre Wedding Photography'),
    		('Photography', 'Maternity Photography'),
    		('Photography', 'Portfolio'),
    		('Application Development','Android Application'),
    		('Application Development','Ios Application'),
    	]
	choice=models.CharField(max_length=50, choices=field_choice)
	email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	message=models.CharField(max_length=100)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name