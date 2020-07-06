from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ResourceView

app_name = 'resources'

urlpatterns = [
    path('resources', ResourceView.as_view(), name='resource'),
]

urlpatterns = format_suffix_patterns(urlpatterns)