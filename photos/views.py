from django.shortcuts import render
from .models import Image
# Create your views here.
def home(request):
    image = Image.display_image()
    context={"image":image}
    return render(request, 'home.html',context)