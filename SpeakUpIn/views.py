#*-* coding: utf-8 *-*
from django.views.generic import TemplateView, ListView, View
from django.shortcuts import get_object_or_404, render, redirect
from SpeakUpIn.models import Ticket
from SpeakUpIn.forms import NewTicketForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.http import Http404

class IndexView(View):
    template_name = "speakup/index.html"
    form_class = NewTicketForm
    success_url = '/speakupinbound'

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if request.user.groups.filter(name='SpeakUp Inbound').exists():
            return render(request, self.template_name, {'form': form})
        else:
            raise Http404

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            SCHOOLS = (
           ('1',("м. Левобережная - ул. Луначарского, 4 6-й этаж")),
           ('2',("м. Университет - ул. М.Коцюбинского, 14 1-й этаж")),
           ('3',("м.Житомирская - пр. Победы 13б, 3-й этаж")),
            ('4',("м.Контрактовая Площадь - ул. Спасская 5, 2-й этаж")),
           )
            place = form.cleaned_data["school"]
            ticket = Ticket.objects.create(phone=form.cleaned_data['phone'],
                                           first_name=form.cleaned_data['first_name'],
                                           last_name=form.cleaned_data['last_name'],
                                           middle_name=form.cleaned_data['middle_name'],
                                           city=form.cleaned_data['city'],
                                           age=form.cleaned_data['age'],
                                           place=place,
                                           is_ticket=True,
                                           owner=self.request.user.last_name,
                                           creation_date=datetime.now(),
                                          )

            return render(request, "layouts/formResult.html", {'form': form, 'ticket_id': ticket.id})

        else:
            return render(request, "layouts/formResult.html", {'form': form, 'formError': True})

        #return render(request, self.template_name, {'form': form})

class RecallView(TemplateView):
    template_name = "speakup/recall.html"

class ShowTicketsView(TemplateView):
    template_name = "speakup/myTickets.html"

class TicketsListView(ListView):
    model = Ticket
    context_object_name = "ticket_list"
    template_name = "speakup/myTickets.html"

    def get_context_data(self, **kwargs):
        context = super(TicketsListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['ticket_list'] = Ticket.objects.filter(owner=self.request.user.last_name)
        return context

class TicketsSearchView(ListView):
    model = Ticket
    context_object_name = "ticket_list"
    template_name = "speakup/myTickets.html"

    def get(self, request, *args, **kwargs):
        kwargs['owner'] = self.request.user.last_name
        for item in self.request.GET:
            kwargs[item] = self.request.GET[item]
            totalItems = Ticket.objects.filter(**kwargs)
        return render(request, self.template_name, {'ticket_list': Ticket.objects.filter(**kwargs)})

