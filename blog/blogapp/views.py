from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry, Speakers, Sponsors
from .enum import GOLD, SILVER, BRONZE
from .forms import ContatoForm
from django.http import HttpResponse
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
    paginate_by = 2

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


def get_name(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST):
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['sender']
                cc_myself = form.cleaned_data['cc_myself']
                context_object_name = 'contato_form'

                recipients = ['info@example.com']
                if cc_myself:
                    recipients.append(sender)

                send_mail(subject, message, sender, recipients)
                return HttpResponseRedirect('/thanks/')

    else:
        form = ContatoForm()

    return render(request, 'name.html', {'form': form})
