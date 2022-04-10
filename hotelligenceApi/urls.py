from django.urls import include, path
from django.contrib import admin
from api.views import (
    AuthLoginViewSet
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-token-auth/', AuthLoginViewSet.as_view(), name='api_token_auth'),
    path('api/', include('api.urls'), name="api"),
    path('admin/', admin.site.urls),
]
