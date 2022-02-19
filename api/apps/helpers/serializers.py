from rest_framework import serializers


class GenericResponseSerializer(serializers.Serializer):
    reason = serializers.CharField()
