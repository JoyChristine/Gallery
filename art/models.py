from django.db import models

# Create your models here.
class Location(models.Model):
    loc_name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.loc_name

class Category(models.Model):
    cat_name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.cat_name
class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='picture/',null=True)
    description = models.TextField(max_length=1000)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()


