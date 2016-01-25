from django.db import models


class Opera(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(
        upload_to='opere/images',
    )

    def str(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Opere'
