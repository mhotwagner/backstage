from rest_framework import serializers

from .models import Foto


class FotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foto
        fields = (
            'name',
            'location',
            'date',
            'image',
            'created',
            'updated'
        )
