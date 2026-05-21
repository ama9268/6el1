from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from core.views import UnderConstructionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    
    # Rutas comentadas para forzar el modo mantenimiento / en construcción
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', include('core.urls')),
    # path('dashboard/', include('dashboard.urls')),
]

# Servir estáticos en desarrollo antes del comodín
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Redirigir cualquier otra petición a la vista de en construcción
urlpatterns += [
    re_path(r'^.*$', UnderConstructionView.as_view(), name='under_construction'),
]
