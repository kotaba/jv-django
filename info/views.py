from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

class MainView(TemplateView):
    template_name = "info/index.html"

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        return render(request, self.template_name)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/')

    return render_to_response('info/login.html', {'current_date': '1'}, RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")
