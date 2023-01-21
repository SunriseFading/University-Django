from django.urls import path

from discipline.views import (
    DisciplineListCreateView,
    DisciplineRetrieveUpdateDestroyView,
)

app_name = "discipline"

urlpatterns = [
    path("", DisciplineListCreateView.as_view(), name="list"),
    path(
        "<int:pk>/",
        DisciplineRetrieveUpdateDestroyView.as_view(),
        name="detail",
    ),
]
