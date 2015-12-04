from django import forms


class EventoForm(forms.Form):
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)
    sender = forms.EmailField()
