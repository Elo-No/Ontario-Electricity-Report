from rest_framework import serializers

from apps.report.models import DemandReport


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandReport
        fields = ("id", "date", "hour", "market_demand", "ontario_demand")
        read_only = ("id",)

    def create(self, validated_data):
        instance, _ = DemandReport.objects.update_or_create(
            date=validated_data["date"],
            hour=validated_data["hour"],
            defaults={
                "market_demand": validated_data["market_demand"],
                "ontario_demand": validated_data["ontario_demand"],
            },
        )
        return instance

    def update(self, instance, validated_data):
        raise NotImplementedError("not implemented")


class BulkReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandReport
        fields = ("id", "name", "date", "hour", "market_demand", "ontario_demand")
        read_only = ("id",)

    def create(self, validated_data):
        DemandReport.objects.bulk_create()
        DemandReport.objects.bulk_update()
        DemandReport.objects.in_bulk()


class CreateReportInputSerializer(serializers.Serializer):
    demand = ReportSerializer(many=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        demand_serializer = self.fields["demand"]
        demand_serializer.create(validated_data.get("demand"))
        return validated_data


# def to_representation(self, instance):
#     return instance.get('demand')
