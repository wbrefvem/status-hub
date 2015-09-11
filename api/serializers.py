from rest_framework import serializers
from status import models


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Status


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Destination
        fields = ('id', 'name')
