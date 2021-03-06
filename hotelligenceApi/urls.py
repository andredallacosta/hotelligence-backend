from django.urls import include, path
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include('api.urls'), name="api"),
    path('admin', admin.site.urls),
]
