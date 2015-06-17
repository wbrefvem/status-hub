from django.conf.urls import include, url
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'statuses', views.StatusViewSet)

urlpatterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls))
]
