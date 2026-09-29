from django.urls import path

from .properties import metrics
from .views import *
urlpatterns = [
    path("", health_endpoint),
    path("metrics/", metric_view),
    path("semantic", semantic_view)
]