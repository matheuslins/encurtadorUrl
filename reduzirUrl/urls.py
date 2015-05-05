from django.conf.urls import patterns, include, url

urlpatterns = patterns('reduzirUrl.views',
    url(r'^$', 'index', name='home'),
    # home/index
 
    url(r'^(?P<short_id>\w{6})$', 'redirectOriginal', name='redirectOriginal'),
    
    url(r'^makeshort/$', 'shortenUrl', name='shortenUrl'),
    # reduzir a URL
)

