from authapp import views
from django.urls import include, path

urlpatterns = [
  
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
   
]
