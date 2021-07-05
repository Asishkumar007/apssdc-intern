from django.db import models

# Create your models here.
class Register(models.model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_lenght=50)


class SignUp(models.model):
	fname=models.CharField(max_length=50)
	age =models.IntegerField()

	class Meta:
		db_table='signup'