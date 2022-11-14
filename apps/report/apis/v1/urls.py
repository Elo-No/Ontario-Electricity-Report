from django.urls import path

from apps.report.apis.v1.views import (
    CreateReportAPIView,
    ListReportAPIView,
    DeleteReportAPIView,
)

app_name = "report_v1"

urlpatterns = [
    path("demand/", CreateReportAPIView.as_view(), name="create_report"),
    path("", ListReportAPIView.as_view(), name="list_report"),
    path("<date:requesteddate>/", DeleteReportAPIView.as_view(), name="delete_report"),
]
