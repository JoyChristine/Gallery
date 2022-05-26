
from django.conf import settings
from . import views
from django.urls import re_path
from django.conf.urls.static import static

urlpatterns = [
    re_path('',views.home,name='home'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
