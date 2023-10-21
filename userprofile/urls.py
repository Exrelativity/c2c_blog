from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("<uuid:userId>/", show),
    path("<uuid:userId>/update/", update),  # Added trailing slashes
    path("create/", create),  # Added a trailing slash
    path("<uuid:userId>/delete", delete),
]
