from django.urls import path
from myapp.views import current_time

urlpatterns = [
    path('current_time/', current_time, name='current_time'),
]
