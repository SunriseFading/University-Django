from django.urls import path
from direction.views import DirectionListCreateView, DirectionRetrieveUpdateDestroyView

app_name = "direction"

urlpatterns = [
    path("", DirectionListCreateView.as_view(), name="list"),
    path(
        "<int:pk>/",
        DirectionRetrieveUpdateDestroyView.as_view(),
        name="detail",
    ),
]
