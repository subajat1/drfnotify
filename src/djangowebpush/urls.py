from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import home, send_push, subscribe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('subscribe/', subscribe),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
