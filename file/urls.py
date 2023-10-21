from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="file.index"),
    path("<uuid:id>/", show, name="file.show"),
    path("upload/", create, name="file.create"),
    path("<uuid:id>/delete/", delete, name="file.delete"),
]
