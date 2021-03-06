from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^news$', 'blogapp.views.blog_news', name='lista'),
    url(r'^speaker$', 'blogapp.views.blog_speaker', name='palestrantes'),
    url(r'^sponsor$', 'blogapp.views.blog_sponsor', name='patrocinadores'),
    url(r'^home$', 'blogapp.views.blog_index', name='home'),
    url(r'^(?P<pk>[\d]+)/$',
        'blogapp.views.blog_publicacoes_detalhes', name='detalhes'),
    url(r'event$', 'blogapp.views.blog_evento', name='evento'),
    url(r'event2$', 'blogapp.forms.criar_speaker', name='evento2'),
    url(r'^thanks$', 'blogapp.views.blog_obrigado', name='agradecimento'),
    url(r'^event', 'blogapp.views.blog_evento', name='evento'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
