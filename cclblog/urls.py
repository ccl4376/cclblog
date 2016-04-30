from django.conf import settings
from django.conf.urls import patterns,include, url
from django.contrib import admin
from blogging import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'),name='contact'),
    url(r'^blogs/(?P<slug>[-\w]+)/$', views.blog_detail, name='blog_detail'),
    url(r'^admin/', include(admin.site.urls)),

]
if settings.DEBUG: urlpatterns += [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
]
