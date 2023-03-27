from django.db import models

# Create your models here.
class Barista(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=25)
    partner_number = models.IntegerField()
    fact =  models.TextField(max_length=250, null=True)
    barista_image = models.ImageField(upload_to="images",default='https://miro.medium.com/v2/resize:fit:720/format:webp/1*EN0fyh1x46dxsc-w20lRfw.jpeg')
    potq = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.role
    
class Manager(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=25)
    partner_number = models.IntegerField()
    fact =  models.TextField(max_length=250, null=True)
    manager_image = models.ImageField(upload_to="images",default='https://miro.medium.com/v2/resize:fit:720/format:webp/1*EN0fyh1x46dxsc-w20lRfw.jpeg')
    potq = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name + ' - ' + self.role