from django.shortcuts import render
from .models import Image
# Create your views here.
def index(request):
    image = Image.objects.all()
    context = {'image':image}
    return render(request, 'index.html',context)