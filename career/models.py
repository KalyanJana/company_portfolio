from django.db import models

class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='product/images',blank=True)
    url =models.URLField(blank=True)

    #this is for showing title in the admin section
    def __str__(self):
        return self.title
