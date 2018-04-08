from rest_framework import serializers

from speedvisionx.models import RaceMatrix


class RaceMatrixViewDetails(serializers.ModelSerializer):
    class Meta:
        model = RaceMatrix
        fields = ["media_id", "network", "surface", "track", "date_id", "event", "video_url"]
