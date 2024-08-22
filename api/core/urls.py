from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', include('gallery.urls')),
    path('testimonials/', include('testimonials.urls')),
]
