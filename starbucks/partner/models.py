from django.db import models

# Create your models here.
class Barista(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=25)
    partner_number = models.IntegerField()
    fact =  models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.name + ' - ' + self.role
    
class Manager(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=25)
    partner_number = models.IntegerField()
    fact =  models.TextField(max_length=250, null=True)
   
    def __str__(self):
        return self.name + ' - ' + self.role