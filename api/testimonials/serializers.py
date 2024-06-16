from rest_framework.serializers import ModelSerializer

from .models import Testimonial


class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
