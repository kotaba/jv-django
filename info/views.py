from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render_to_response
from django.template import RequestContext

class MainView(TemplateView):
    template_name = "info/index.html"

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
    return render_to_response('info/login.html', {'current_date': '1'}, RequestContext(request))
    