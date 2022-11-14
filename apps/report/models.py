from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.core.models import BaseModel


class DemandReport(BaseModel):
    date = models.DateTimeField(_("Date"))
    hour = models.PositiveIntegerField(_("Hour"))
    market_demand = models.PositiveIntegerField(_("Market Demand"))
    ontario_demand = models.PositiveIntegerField(_("Ontario Demand"))
    market_peak_day = models.BooleanField(_("Market Peak Day"), blank=True, null=True)
    Ontario_peak_day = models.BooleanField(_("Ontario Peak Day"), blank=True, null=True)
    market_peak_month = models.BooleanField(
        _("Market Peak Month"), blank=True, null=True
    )
    ontario_peak_month = models.BooleanField(
        _("Ontario Peak Month"), blank=True, null=True
    )

    class Meta:
        unique_together = ["date", "hour"]

    def __str__(self):
        return f"{self.date} - {self.ontario_demand}"
