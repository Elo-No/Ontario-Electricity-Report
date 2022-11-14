from django.urls import path, include

urlpatterns = [
    path("api/v1/reports/", include("report.apis.v1.urls", namespace="api_v1")),
    # api/v1/reports/?start =date & end = date filterset
    # api/v1/reports/2022-12-11/12 delet_perform
]
