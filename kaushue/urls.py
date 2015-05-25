from django.conf.urls import patterns, url
from kaushue import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^partial/(?P<question_id>\d+)/$', views.partial, name='partial'),
    url(r'^edit/(?P<question_id>\d+)/$', views.edit, name='edit'),
    url(r'^add_link/$', views.add_link, name='add_link'),
    url(r'^remove_link/$', views.remove_link, name='remove_link'),
    url(r'^new/$', views.new, name='new'),
)
