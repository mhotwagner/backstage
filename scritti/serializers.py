from rest_framework import serializers

from .models import Scritto


class ScrittoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scritto
        fields = (
            'id',
            'name',
            'publication',
            'link',
            'date',
            'image',
            'created',
            'updated'
        )
