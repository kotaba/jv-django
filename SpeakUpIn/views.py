from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "speakup/index.html"

class RecallView(TemplateView):
    template_name = "speakup/recall.html"

class ShowTicketsView(TemplateView):
    template_name = "speakup/myTickets.html"
