from django.db import models
from partner.models import Barista


# Create your models here.
class Review(models.Model):
    drink_name = models.CharField(max_length=50)
    partner_name = models.ManyToManyField(
    Barista, blank=True, related_name="partner_name")
    customization = models.TextField(max_length=1000, null=True)
    drink_image = models.ImageField(upload_to="images", default='https://miro.medium.com/v2/resize:fit:720/format:webp/1*EN0fyh1x46dxsc-w20lRfw.jpeg')

    def __str__(self):
        return self.drink_name
    

