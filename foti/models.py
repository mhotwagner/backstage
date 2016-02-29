from django.db import models

from opere import models as opere_models


class Foto(opere_models.Opera):
    foto_index = models.IntegerField(default=0, blank=False, null=False)

    location = models.CharField(max_length=64, blank=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Foti'
        ordering = ('foto_index',)

    def save(self, *args, **kwargs):
        self.is_foto = True
        super(Foto, self).save(*args, **kwargs)
