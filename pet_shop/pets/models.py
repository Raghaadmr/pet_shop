from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerFeild()
    available= model.BooleanFeild(null=True)
    price=model.DecimalFeild()
    image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name
