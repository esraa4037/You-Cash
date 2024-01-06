from django.urls import path
from . import views


urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path(
        "<int:account_id>/transaction-history",
        views.transaction_history,
        name="transaction_history",
    ),
    path("<int:account_id>/", views.account_details, name="account_details"),
    path("test_token", views.test_token, name="test_token"),
]
