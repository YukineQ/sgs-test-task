from django.contrib import admin
from django.urls import path, include

api_prefix = 'api'

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f'{api_prefix}/', include('accounts.urls')),
    path(f'{api_prefix}/', include('images.urls'))
]
