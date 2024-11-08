
from django.contrib import admin # type: ignore
from django.urls import path, re_path, include # type: ignore
from applications.exp.views import IndexView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.empleados.urls')),
    re_path('', include('applications.exp.urls')),
    re_path('', include('applications.departamentos.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



