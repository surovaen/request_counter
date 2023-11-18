from rest_framework import serializers


class CounterSerializer(serializers.Serializer):
    """Сериалайзер количества запросов."""

    id = serializers.IntegerField(read_only=True)
    count = serializers.IntegerField(read_only=True)
