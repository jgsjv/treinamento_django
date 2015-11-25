from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^news$', 'blogapp.views.blog_news', name='lista'),
    url(r'^speaker$', 'blogapp.views.blog_speaker', name='palestrantes'),
    url(r'^sponsor$', 'blogapp.views.blog_sponsor', name='patrocinadores'),
    url(r'^home$', 'blogapp.views.blog_index', name='home'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
