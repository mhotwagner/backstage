from django.db import models

from solo.models import SingletonModel
from phonenumber_field import modelfields as phonenumber_models


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
