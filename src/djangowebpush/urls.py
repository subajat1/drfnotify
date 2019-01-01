from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView


from .views import home, send_push

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', home),
    url(r'^send_push', send_push),
    url(r'^webpush/', include('webpush.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
