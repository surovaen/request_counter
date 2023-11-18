from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from backend.api.v1.counter.serializers import CounterSerializer
from backend.counter.models import Counter


COUNTER_METHOD_MAP = {
    1: Counter.lock_table_increase_counter,
    2: Counter.lock_row_increase_counter,
    3: Counter.database_increase_counter,
}


@api_view(['GET'])
def counter(request, id: str):
    """Эндпоинт для подсчета количества запросов."""

    COUNTER_METHOD_MAP[int(id)](pk=int(id))
    return Response(status=status.HTTP_200_OK)


class CounterViewSet(ListModelMixin, GenericViewSet):
    """Вьюсет счетчика запросов."""

    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
