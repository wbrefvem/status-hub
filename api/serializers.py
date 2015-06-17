from rest_framework import serializers
from status import models


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contact


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Department


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Status
