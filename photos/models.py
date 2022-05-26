from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=60,primary_key=True)
    id = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='picture/', null=True)
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        image = cls.objects.all()
        return image
    



class Location(models.Model):
    loc_name = models.CharField(max_length=60)

    def __str__(self):
        return self.loc_name

class Category(models.Model):
    cat_name= models.CharField(max_length=60)
    
    def  __str__(self):
        return self.cat_name
