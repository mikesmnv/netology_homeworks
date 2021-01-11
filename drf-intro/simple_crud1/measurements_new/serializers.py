from rest_framework import serializers
from models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "latitude", "longitude", "created_at", "updated_at")


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ("id", "project", "created_at", "updated_at")
