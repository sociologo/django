from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static  # type: ignore

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include("applications.empleados.urls")),
   path('', include("applications.exp.urls")),
   path('', include("applications.departamentos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
