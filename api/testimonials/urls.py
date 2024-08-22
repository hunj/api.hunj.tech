from django.urls import path
from . import views

urlpatterns = [
    path("", views.TestimonialsListAPIView.as_view(), name="testimonials_list"),
]
