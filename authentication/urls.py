from django.urls import path
from .views import login_view, logout_view, register_user, forgot_password, update_password, confirm_email

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_user, name="register"),
    path("password/forgot/", forgot_password, name="forgot-password"),
    path("password/update/<uuid:id>/<str:token>/", update_password, name="update-password"),
    path("confirm/email/<str:email>/", confirm_email, name="confirm-email"),
]
