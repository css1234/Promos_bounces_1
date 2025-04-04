from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('users/', include('apps.users.url')),  # Include the users app URLs
    path('users/',include('apps.users.url')),
    path('', include('apps.employee.urls')),  # Include the employee app URLs
    path('', include('apps.step_stage.urls')),  # Include the step_stage app URLs
    path('', include('apps.promos.urls')),  # Include the promos app URLs
]
