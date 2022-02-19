from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', include('api.apps.reason.urls')),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]