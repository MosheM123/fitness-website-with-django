from django.db import models

# Create your models here.

class Products(models.Model):
  itsname = models.CharField(max_length=255)
  price = models.IntegerField()
  img = models.ImageField(null=True, blank=True, upload_to='images/')

  def __str__(self):
        return self.itsname