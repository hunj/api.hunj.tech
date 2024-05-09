from django.urls import path, include


urlpatterns = [
    path('photos/', include('photos.urls')),
]
