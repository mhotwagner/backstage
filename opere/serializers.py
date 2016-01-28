from rest_framework import serializers

from .models import Opera


class OperaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opera
        fields = (
            'id',
            'name',
            'image',
            'created',
            'updated'
        )
