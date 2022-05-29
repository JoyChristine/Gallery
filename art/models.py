from django.db import models

# Create your models here.
class Location(models.Model):
    loc_name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.loc_name

    def save_location(self):
        self.save()

    @classmethod
    def filter_by_location(cls,location):
        images = cls.objects.filter(location__loc_name__icontains=location)
        return images

    def delete_(self):
        self.delete()

    @classmethod
    def update_location(cls,location):
        cls.objects.filter(loc_name=location).update(loc_name=location)

class Category(models.Model):
    cat_name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.cat_name

    def save_category(self):
        self.save()

    def delete(self):
        self.delete()

    @classmethod
    def update_category(cls, category):
        cls.objects.filter(cat_name=category).update(cat_name=category)


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
# delete,update
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__cat_name__icontains=search_term)
        return images
   

    @classmethod
    def filter_by_location(cls,location):
        images = cls.objects.filter(location__loc_name__icontains=location)
        return images

    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,image):
       cls.objects.filter(id=id).update(image=image)

    @classmethod
    def get_image_by_id(cls,id):
        cls.objects.filter(id=id)
