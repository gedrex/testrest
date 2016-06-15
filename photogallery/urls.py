from django.conf.urls import *
from .views import PhotoJSONListView
from photologue.views import GalleryListView
from django.views.generic import TemplateView

urlpatterns = patterns('',

						url(r'^gallerylist/$', GalleryListView.as_view(), name='photogallery-gallery-list'),
						url(r'^photolist/$', PhotoJSONListView.as_view(), name='photogallery-photo-json-list'),
                       )
