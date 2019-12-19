from django.db import models

# Create your models here.

class UserInfo(models.Model):
	name = models.CharField(max_length=30,null=True)
	email = models.EmailField(max_length=30,null=True)
	phone_number = models.IntegerField(null=True)
	date_of_birth = models.CharField(max_length=30,null=True)

	def __str__(self):
		return self.name
