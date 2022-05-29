from django.shortcuts import render
from .models import Image
# Create your views here.
def index(request):
    image = Image.objects.all()
    context = {'image':image}
    return render(request, 'all/index.html',context)

def search(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all/search.html',{'message':message,'images':searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all/search.html',{'message':message})

