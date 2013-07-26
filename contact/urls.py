from django.conf.urls import patterns, url

from .views import SubmitView, ThanksView


urlpatterns = patterns('',
    url(r'^$', SubmitView.as_view(), name='form'),
    url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
)
