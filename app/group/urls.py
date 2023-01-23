from django.urls import path

from group.views import GroupListCreateView, GroupRetrieveUpdateDestroyView

app_name = "group"

urlpatterns = [
    path("", GroupListCreateView.as_view(), name="list"),
    path("<int:pk>/", GroupRetrieveUpdateDestroyView.as_view(), name="detail"),
]
