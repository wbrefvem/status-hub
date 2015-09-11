from django.conf.urls import include, url
from rest_framework import routers
from api import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'statuses', views.StatusViewSet)
router.register(r'destinations', views.DestinationViewSet)

urlpatterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls))
]
