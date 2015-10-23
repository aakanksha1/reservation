from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<restaurant_name>[,\w\d\s_&]+)/(?P<restaurant_address>[,\w\d\s_]+)/$', views.restaurant, name='restaurant'),
    url(r'^(?P<restaurant_name>[,\w\d\s_&]+)/(?P<restaurant_address>[,\w\d\s_]+)/update_wait_time/$', views.update_wait_time, name='update_wait_time'),
    url(r'^(?P<restaurant_name>[,\w\d\s_&]+)/(?P<restaurant_address>[,\w\d\s_]+)/new_eatsat/$', views.new_eatsat, name='new_eatsat'),
    url(r'^(?P<restaurant_name>[,\w\d\s_&]+)/(?P<restaurant_address>[,\w\d\s_]+)/cancel_eatsat/(?P<account_id>[\d]+)/$', views.cancel_eatsat, name='cancel_eatsat'),

    
]
