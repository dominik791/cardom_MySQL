from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^flats/', views.flats, name='flats'),
    url(r'^houses/', views.houses, name='houses'),
    url(r'^lots/', views.lots, name='lots'),
    url(r'^locals/', views.locals, name='locals'),
    url(r'^objects/', views.other_objects, name='other_objects'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^career/', views.career, name='career'),
    url(r'^publish_offer/', views.publish_offer, name='publish_offer'),
    url(r'^offer_list/', views.offer_list, name='offer_list'),
    )