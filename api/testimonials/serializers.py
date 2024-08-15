from rest_framework import serializers

from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = '__all__'

    def get_icon(self, obj):
        return obj.icon.url
