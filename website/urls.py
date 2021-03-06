"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from SpeakUpIn import urls as speakurls
from ajax import urls as ajaxurls
from info.views import MainView
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainView.as_view()),
    url(r'^login/', 'info.views.login', name='login'),
    url(r'^logout/', 'info.views.logout', name='logout'),
    url(r'^speakupinbound/', include(speakurls)),
    url(r'^ajax/', include(ajaxurls)),

]

admin.site.site_header = 'JV Call Center'
