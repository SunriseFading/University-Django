from django.urls import path

from curator.views import CuratorListCreateView, CuratorRetrieveUpdateDestroyView

app_name = "curator"


urlpatterns = [
    path("", CuratorListCreateView.as_view(), name="list"),
    path("<int:pk>/", CuratorRetrieveUpdateDestroyView.as_view(), name="detail"),
]
