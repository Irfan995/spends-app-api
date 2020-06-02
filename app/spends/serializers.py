from rest_framework import serializers
from core.models import Spend


class SpendSerializer(serializers.ModelSerializer):
    """
    Serializer for spend object
    """

    class Meta:
        model = Spend
        fields = ('id', 'item', 'date', 'quantity', 'price')
        read_only_field = ('id',)
