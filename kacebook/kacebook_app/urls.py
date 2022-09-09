"""defines urls patterns for learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    url(r'^new_message/$', views.new_message, name='new_message'),
    url(r'^(?P<user_id>\d+)/$', views.profile, name='profile'),
    url(r'^friends/$', views.friends, name='friends'),

]
