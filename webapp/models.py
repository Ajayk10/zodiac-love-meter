from django.db import models
from datetime import datetime 

# ...
# Create your models here.


class Contact(models.Model):
	your_name = models.CharField(max_length=20 ,null=True)
	your_partner_name = models.CharField(max_length=100 ,null=True)
	your_star = models.CharField(max_length=100,null=True)
	your_partner_star = models.CharField(max_length=100 ,null=True)
	feel = models.CharField(max_length=100 ,null=True)


	def __str__(self):
		return self.your_name +'---> '+ self.your_partner_name



