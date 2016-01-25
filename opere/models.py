from django.db import models


class Opera(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(
        upload_to='opere/images',
    )

    def str(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Opere'
