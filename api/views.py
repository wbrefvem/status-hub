from rest_framework import viewsets
from status import models
from status.tasks import post_status_to_corecon
from api import serializers, renderers, parsers


class BaseViewSet(viewsets.ModelViewSet):
    renderer_classes = (renderers.JSONRenderer,)
    parser_classes = (parsers.JSONParser,)


class StatusViewSet(BaseViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

    def create(self, request, *args, **kwargs):
        response = super(StatusViewSet, self).create(request, *args, **kwargs)

        post_status_to_corecon.delay(response.data)

        return response

    def update(self, request, *args, **kwargs):
        return super(StatusViewSet, self).update(request, *args, **kwargs)


class DestinationViewSet(BaseViewSet):
    queryset = models.Destination.objects.all()
    serializer_class = serializers.DestinationSerializer
