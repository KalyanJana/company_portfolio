from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    image = models.ImageField(upload_to='product/images')
    url =models.URLField(blank=True)

    #this is for showing title in the admin section
    def __str__(self):
        return self.title
