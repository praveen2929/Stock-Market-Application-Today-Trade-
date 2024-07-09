from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class course(models.Model):
    title = models.CharField(max_length=1000)
    number=models.IntegerField(default=0)
    image1 = models.ImageField(upload_to='image',default='static\image\email.png')
    desc = HTMLField()
   
