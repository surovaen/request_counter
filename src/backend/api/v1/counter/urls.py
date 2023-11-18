from django.urls import path
from rest_framework.routers import DefaultRouter

from backend.api.v1.counter.views import CounterViewSet, counter


router = DefaultRouter()
router.register('count', CounterViewSet)

urlpatterns = [
    path('counter/<id>/', counter),
]

urlpatterns += router.urls
