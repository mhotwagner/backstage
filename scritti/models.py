from django.db import models

from opere import models as opere_models


class Scritto(opere_models.Opera):
    publication = models.CharField(max_length=64, blank=False)
    link = models.URLField(blank=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Scritti'

    def save(self, *args, **kwargs):
        self.is_scritto = True
        super(Scritto, self).save(*args, **kwargs)
