from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("curator/", include("curator.urls")),
    path("direction/", include("direction.urls")),
    # path("discipline/", include("discipline.urls")),
    # path("group/", include("group.urls")),
    # path("student/", include("student.urls")),
]
