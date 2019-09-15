from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contents', views.ContentViewSet)
router.register(r'messages', views.MessageViewSet)

schema_view = get_schema_view(title='Pollen API')
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
]