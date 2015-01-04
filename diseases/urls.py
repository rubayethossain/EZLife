from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'diseases.views.index', name='Homepage'),
)
