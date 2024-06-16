from rest_framework.generics import ListAPIView

from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialsListAPIView(ListAPIView):
    lookup_field = 'uuid'
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all()
