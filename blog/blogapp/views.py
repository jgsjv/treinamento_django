from django.shortcuts import render
from django.views.generic import ListView
from .models import Entry, Speakers, Sponsors
from .enum import GOLD, SILVER, BRONZE


class BlogIndex(ListView):
    queryset = Entry.objects.published()
    template_name = "blogapp/home.html"
    paginate_by = 2

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
