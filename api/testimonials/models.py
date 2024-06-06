from django.db import models
from common.models import BaseModel

class Testimonial(BaseModel):
    icon = models.ImageField()
    name = models.TextField(max_length=32)
    username = models.TextField(max_length=32)
    link = models.URLField()
    comment = models.TextField()
