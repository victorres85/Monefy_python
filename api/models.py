from django.db import models

# Create your models here.

class Caterogies(models.Model):
    pass

class Account(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    balance = models.FloatField()
    image = models.ImageField()

    def __unicode__(self):
        return self.name