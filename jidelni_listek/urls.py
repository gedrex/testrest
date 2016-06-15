from django.conf.urls import url, include, patterns


from jidelni_listek import views

app_name='jidelni_listek'
urlpatterns = patterns('jidelni_listek.views', 
    url(r'^$', 'index'),
    url(r'^(?P<list_id>[0-9]+)/$', views.detail, name='detail'),
)
