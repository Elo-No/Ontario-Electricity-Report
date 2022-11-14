from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from django_filters import FilterSet, filters
from apps.report.apis.v1.serializers import (
    ReportSerializer,
    CreateReportInputSerializer,
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from apps.report.models import DemandReport


class CreateReportAPIView(CreateAPIView):
    """
    Create demand objects
    :param :
    :return:
    """

    serializer_class = CreateReportInputSerializer


class ReportFilter(FilterSet):
    date_start = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_end = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = DemandReport
        fields = ["date"]


class ListReportAPIView(ListAPIView):
    """
    List demand objects
    :param :
    :return:
    """

    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = ReportFilter

    def get_queryset(self):
        return DemandReport.objects.all()


class DeleteReportAPIView(UpdateAPIView):
    """
    Soft delete demand objects
    :param :
    :return:
    """

    serializer_class = ReportSerializer

    # TODO:Optimize the soft delete
    def perform_update(self, serializer):
        items = DemandReport.objects.filter(date=self.request.get("date"))
        for item in items:
            item.update(is_deleted=True)
            item.save()
