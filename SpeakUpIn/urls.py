from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^/', IndexView.as_view()),
]
