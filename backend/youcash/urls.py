from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from transactions import views


urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("tokenrequest/", obtain_auth_token),
    path("transactions/", include("transactions.urls")),
    path("admin/", admin.site.urls),
]
