from rest_framework import viewsets
from status import models
from api import serializers, renderers


class BaseViewSet(viewsets.ModelViewSet):
    renderer_classes = (renderers.JSONRenderer,)


class ContactViewSet(BaseViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class DepartmentViewSet(BaseViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class StatusViewSet(BaseViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
