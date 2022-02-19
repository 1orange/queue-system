from rest_framework import serializers
from .models import MedicalReason


class MedicalReasonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    reason = serializers.CharField(max_length=255)
    execution_time = serializers.IntegerField()
    parallelizable = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        return MedicalReason.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        instance.reason = validated_data.get('reason', instance.reason)
        instance.execution_time = validated_data.get('executon_time', instance.execution_time)
        instance.paralelelizable = validated_data.get('paralelelizable', instance.paralelelizable)

        instance.save()

        return instance