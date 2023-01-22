from celery.result import AsyncResult
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from task.tasks import create_report


class ReportCreateView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        task = create_report.delay()
        return Response(data={"task_id": task.id}, status=status.HTTP_202_ACCEPTED)


class ReportRetrievalView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, task_id):
        task = AsyncResult(task_id)
        if task.state != "SUCCESS":
            return Response(data={"status": task.state}, status=status.HTTP_200_OK)
        report = open(f"media/{task.result}", "rb")
        response = HttpResponse(
            content=report,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = f"attachment; filename={task.result}"
        return response
