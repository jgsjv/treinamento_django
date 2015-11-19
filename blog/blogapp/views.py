from django.shortcuts import render
from django.views.generic import ListView
from .models import Entry, Speakers, Sponsors


class BlogIndex(ListView):
    queryset = Entry.objects.published()
    template_name = "blogapp/home.html"
    paginate_by = 5

blog_index = BlogIndex.as_view()


class SpeakerIndex(ListView):
    queryset = Speakers.objects.all()
    template_name = "blogapp/home.html"

blog_speaker = SpeakerIndex.as_view()


class SponsorIndex(ListView):
    queryset = Sponsors.objects.all()
    template_name = "blogapp/home.html"

blog_sponsor = SponsorIndex.as_view()
