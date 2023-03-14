from django.db import models

# Create your models here.
class Partner(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=25)
    partner_number = models.IntegerField()
    coffee_master = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name + ' - ' + self.role