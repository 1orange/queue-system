from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.apps.reason import views

urlpatterns = [
    path("reason/", views.ReasonsListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
