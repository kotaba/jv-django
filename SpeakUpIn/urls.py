from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from views import IndexView

urlpatterns = [
    url(r'^', IndexView.as_view()),
]

#http://djbook.ru/rel1.8/topics/auth/default.html
