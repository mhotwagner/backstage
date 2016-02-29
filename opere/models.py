from django.db import models

from imagekit import models as imagekit_models
from imagekit.processors import Adjust


IMAGE_DIR = 'opere/images'


class Opera(models.Model):
    opera_index = models.IntegerField(default=0, blank=False, null=False)

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

    is_foto = models.BooleanField(default=False)
    is_scritto = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Opere'
        ordering = ('opera_index',)
