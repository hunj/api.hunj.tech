from django.urls import path, include


urlpatterns = [
    path('gallery/', include('gallery.urls')),
]
