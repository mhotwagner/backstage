from django.db import models

from solo.models import SingletonModel
from phonenumber_field import modelfields as phonenumber_models

from foti.models import Foto
from opere.models import Opera
from scritti.models import Scritto


class Profile(SingletonModel):

    name = models.CharField(
            max_length=255,
            blank=False,
    )
    _title = models.CharField(
        max_length=255,
        blank=True,
        help_text='Site title used in tab. Defaults to \'name\' if left blank.',
    )
    tagline = models.CharField(
        max_length=515,
        blank=True,
        help_text='Just a quick description (e.g. "Waddling through the world in search of adventure and snuggles" to go with "Nomad Penguin"',
    )
    intro = models.TextField(
        max_length=1024,
        blank=True,
    )
    bio_title = models.CharField(max_length=64, blank=True)
    bio = models.TextField(
        max_length=4096,
        blank=True,
    )

    # Contact Info
    _contact_name = models.CharField(
        max_length=64,
        blank=True,
        help_text='Just in case you didn\'t use your real name up above. You can leave this blank if you want.',
    )
    address = models.CharField(
        max_length=64,
        blank=True,
    )
    city = models.CharField(
        max_length=64,
        blank=True,
    )
    state = models.CharField(
        max_length=64,
        blank=True,
    )
    country = models.CharField(
        max_length=128,
        blank=True
    )
    zip_code = models.CharField(
        max_length=16,
        blank=True,
        help_text='"Postal Code", technically.'
    )

    email = models.EmailField(
            max_length=128,
            blank=True
    )
    phone = phonenumber_models.PhoneNumberField(blank=True)
    website = models.URLField(blank=True, help_text='In case you have another one, I guess?')
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    pinterest = models.URLField(blank=True)

    # Someday we'll change the first one to accept Opera
    homepage_features = models.ManyToManyField(Opera, related_name='facade_old_homepage_features', help_text='Max of 6!', blank=True)
    new_homepage_features = models.ManyToManyField(Scritto, related_name='facade_homepage_features', help_text='Max of 6!', blank=True)
    writing_features = models.ManyToManyField(Scritto, related_name='facade_writing_features', help_text='Max of 6!', blank=True)
    photo_features = models.ManyToManyField(Foto, related_name='facade_photo_features', help_text='Max of 6!', blank=True)

    @property
    def title(self):
        return self._title or self.name

    @property
    def fullname(self):
        return self._contact_name or self.name
