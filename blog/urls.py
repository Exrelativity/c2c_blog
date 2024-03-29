"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *
from graphene_django.views import GraphQLView
from django.conf import settings
from django.conf.urls.static import static
from .schema import schema

urlpatterns = [
    path("", index),
    path("search", search),
    path("dashboard", dashboard),
    path("about", about),
    path("contact", contact),
    path("faq", faq),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path("media/", include('file.urls')),
    path("admin/", admin.site.urls),
    path("profile/", include('userprofile.urls')),
    path("posts/", include('post.urls')),
    path("", include("authentication.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    ]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)