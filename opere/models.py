from django.db import models

from imagekit import models as imagekit_models
from imagekit.processors import Adjust



IMAGE_DIR = 'opere/images'


class Opera(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    image_color = models.ImageField(
        upload_to=IMAGE_DIR,
    )
    image_grayscale = imagekit_models.ImageSpecField(
        source='image_color',
        processors=[Adjust(color=0), ],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Opere'
