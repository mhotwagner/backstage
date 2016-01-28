from rest_framework import serializers

from .models import Opera


class OperaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opera
        fields = (
            'name',
            'image',
            'created',
            'updated'
        )
