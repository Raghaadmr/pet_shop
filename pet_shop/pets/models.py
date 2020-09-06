from django.db import models
from django.urls import reverse

class Pets(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    available= models.BooleanField(null=True)
    price=models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'pet_id':self.id})
