"""
URL configuration for commander_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.templatetags.static import static as static_url
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("timekeeper/", include("apps.timekeeper.urls")),
    path(
        "images/",
        include(
            "apps.image_processor.urls",
            namespace="images",
        ),
    ),
    re_path(
        r"^favicon\.ico$",
        RedirectView.as_view(
            url=static_url("img/favicons/favicon.ico"), permanent=True
        ),
    ),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
            path("__debug__/", include("debug_toolbar.urls")),
        ]
    )
