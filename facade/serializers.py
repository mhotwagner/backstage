from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'name',
            'title',
            'tagline',
            'intro',
            'bio_title',
            'bio',
            'address',
            'city',
            'state',
            'country',
            'zip_code',
            'email',
            'phone',
            'website',
            'twitter',
            'facebook',
            'instagram',
            'linkedin',
            'pinterest',
        )
