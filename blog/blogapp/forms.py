# -*- coding: utf-8 -*-

from django import forms
from .models import Speakers
from django.shortcuts import render


class EventoForm(forms.Form):
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)
    sender = forms.EmailField()


class SpeakerModelForm(forms.ModelForm):

    class Meta:
        model = Speakers
        fields = '__all__'


def criar_speaker(request):
    if request.method == 'POST':
        spk = SpeakerModelForm(request.POST, request.FILES)
        if spk.is_valid():
            spk.save()
            return HttpResponseRedirect("blogapp/agradecimento.html")
    else:
        spk = SpeakerModelForm()
    return render(request, "blogapp/evento2.html", {'spk': spk})
