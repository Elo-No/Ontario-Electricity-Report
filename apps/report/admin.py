from django.contrib import admin

from apps.report.models import DemandReport


@admin.register(DemandReport)
class DemandReportAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "hour", "market_demand", "ontario_demand")
