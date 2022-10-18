from django.db import models

# Create your models here.

class Caterogies(models.Model):
    pass

class Account(models.Model):
    name = models.CharField(max_length=200)
    #categories = models.ForeignKey(Caterogies, on_delete=models.CASCADE)
    balance = models.FloatField(blank=True)
    image = models.ImageField(upload_to='media/account/%y/%m/%d', blank=True)

    def __unicode__(self):
        return self.name