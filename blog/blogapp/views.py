from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Entry, Speakers, Sponsors
from .enum import GOLD, SILVER, BRONZE
from .forms import EventoForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


class PublicacoesDetalhes(DetailView):
    model = Entry
    template_name = "blogapp/publicacoes_detalhes.html"

blog_publicacoes_detalhes = PublicacoesDetalhes.as_view()


class NewsIndex(ListView):
    queryset = Entry.objects.published()
    template_name = "blogapp/news.html"
    context_object_name = 'news'
    paginate_by = 4

blog_news = NewsIndex.as_view()


class BlogIndex(ListView):
    queryset = Entry.objects.published()
    context_object_name = 'entries'
    template_name = "blogapp/home.html"

    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['GOLD'] = GOLD
        context['SILVER'] = SILVER
        context['BRONZE'] = BRONZE
        context['speakers'] = Speakers.objects.all()
        context['sponsors'] = Sponsors.objects.all()
        return context

blog_index = BlogIndex.as_view()


class SpeakerIndex(ListView):
    queryset = Speakers.objects.all()
    template_name = "blogapp/speakerList.html"
    context_object_name = 'speakers'
    paginate_by = 1

blog_speaker = SpeakerIndex.as_view()


class SponsorIndex(ListView):
    queryset = Sponsors.objects.all()
    template_name = "blogapp/sponsorList.html"
    context_object_name = 'sponsors'

    def get_context_data(self, **kwargs):
        context = super(SponsorIndex, self).get_context_data(**kwargs)
        context['GOLD'] = GOLD
        context['SILVER'] = SILVER
        context['BRONZE'] = BRONZE
        return context

blog_sponsor = SponsorIndex.as_view()


class EventoView(FormView):
    template_name = "blogapp/evento.html"
    form_class = EventoForm
    success_url = "thanks"

blog_evento = EventoView.as_view()


class ThanksView(TemplateView):
    template_name = "blogapp/agradecimento.html"

blog_obrigado = ThanksView.as_view()
