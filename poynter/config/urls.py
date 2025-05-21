from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from cosmos.apps.core.views.home import home

urlpatterns = [
    path("", home, name="home"),
    path("direct_upload/", include("cosmos.apps.direct_upload.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("equipment/", include("cosmos.apps.equipment.urls")),
    path("locations/", include("cosmos.apps.locations.urls")),
    path("tasks/", include("cosmos.apps.tasks.urls")),
    path("rt_messages/", include("pluto_rt.urls")),
    path("tools/", include("cosmos.apps.tools.urls")),
    path("-/", include("django_alive.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
