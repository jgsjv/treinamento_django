from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^lista/$', 'blogapp.views.blog_index', name='lista'),
    url(r'^speaker', 'blogapp.views.blog_speaker', name='palestrantes')

]
