from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include('api.urls'), name="api"),
    path('admin/', admin.site.urls),
]
