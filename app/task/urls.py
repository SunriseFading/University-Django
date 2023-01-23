from django.urls import path

from task.views import ReportCreateView, ReportRetrievalView

app_name = "task"

urlpatterns = [
    path("report/", ReportCreateView.as_view(), name="create_report"),
    path("report/<str:task_id>/", ReportRetrievalView.as_view(), name="retrive_report"),
]
