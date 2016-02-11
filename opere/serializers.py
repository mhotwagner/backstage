from rest_framework import serializers

from .models import Opera


class OperaSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Opera
        fields = (
            'id',
            'name',
            'image',
            'created',
            'updated'
        )
