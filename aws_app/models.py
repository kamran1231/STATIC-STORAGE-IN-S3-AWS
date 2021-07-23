from django.db import models
# from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.


class Photo(models.Model):
    name = models.CharField(max_length=50,null=False)
    image = models.ImageField(null=False,blank=False)

    publish = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


