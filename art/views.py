from unicodedata import category
from django.shortcuts import render
from .models import Image
# Create your views here.
def index(request):
    image = Image.objects.all()
    location = Image.objects.all()
    category = Image.objects.all()
    context = {'images':image, 'location':location, 'category':category}
    return render(request, 'all/index.html',context)

def filter_location(request, location_id):
    images = Image.filter_by_location(location_id)
    return render(request, 'all/filter_location.html',{'images':images})


def search(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all/search.html',{'message':message,'images':searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all/search.html',{'message':message})

