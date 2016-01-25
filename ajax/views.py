from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from SpeakUpIn.models import Ticket
from django.views.generic import View
import json

class PersonalTicketsView(View):

    def get(self, request, *args, **kwargs):
            tickets = Ticket.objects.filter(owner=request.user.last_name)
            return JsonResponse(self.serializer(tickets), safe=False)


    def serializer(self, query):
        iTotalRecords =  len(query)
        iTotalDisplayRecords = 10
        sEcho = 10

        data = []
        for item in query:
                data.append([item.id,
                                       item.getFullName(),
                                       item.phone,
                                       item.city,
                                       item.age,
                                       item.place,
                                       str(item.creation_date)])


