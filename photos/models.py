from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=60,primary_key=True)
    id = models.CharField(max_length=20)
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class Location(models.Model):
    loc_name = models.CharField(max_length=60)

    def __str__(self):
        return self.loc_name

class Category(models.Model):
    cat_name= models.CharField(max_length=60)
    
    def  __str__(self):
        return self.cat_name
