from rest_framework import serializers

class ElevationMapSerializer(serializers.Serializer):
    elevation_data = serializers.CharField()
    show_path = serializers.BooleanField()