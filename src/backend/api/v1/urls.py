from django.urls import include, path

from backend.api.v1.counter import urls as urls_endpoint


urlpatterns = [
    path('endpoint/', include(urls_endpoint)),

]
