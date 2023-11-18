from django.db import connection, models, transaction
from django.db.models import F


class Counter(models.Model):
    """Модель счетчика запросов."""

    count = models.IntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Счетчик запросов'
        verbose_name_plural = 'Счетчик запросов'

    def __str__(self):
        return f'Счетчик запросов {self.pk}'

    @classmethod
    def lock_table_increase_counter(cls, pk: int) -> None:
        """Метод увеличения счетчика путем блокировки таблицы."""

        with transaction.atomic(), connection.cursor() as cursor:
            cursor.execute(
                'LOCK TABLE {} IN EXCLUSIVE MODE;'.format(
                    cls._meta.db_table,
                ),
            )
            endpoint, _ = Counter.objects.get_or_create(pk=pk)
            endpoint.count += 1
            endpoint.save()

    @classmethod
    def lock_row_increase_counter(cls, pk: int) -> None:
        """Метод увеличения счетчика путем блокировки строки."""

        with transaction.atomic():
            endpoint, _ = cls.objects.select_for_update().get_or_create(pk=pk)
            endpoint.count += 1
            endpoint.save()

    @classmethod
    def database_increase_counter(cls, pk: int):
        """Метод увеличения счетчика на уровне базы данных."""

        endpoint, _ = cls.objects.get_or_create(pk=pk)
        endpoint.count = F('count') + 1
        endpoint.save()
