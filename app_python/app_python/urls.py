from django.urls import path
from myapp.views import current_time, visits

urlpatterns = [
    path('current_time/', current_time, name='current_time'),
    path('visits/', visits, name="visits")
]
