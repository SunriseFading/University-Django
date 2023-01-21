from django.urls import path

from student.views import StudentListCreateView, StudentRetrieveUpdateDestroyView

app_name = "student"

urlpatterns = [
    path("", StudentListCreateView.as_view(), name="list"),
    path(
        "<int:pk>/",
        StudentRetrieveUpdateDestroyView.as_view(),
        name="detail",
    ),
]
