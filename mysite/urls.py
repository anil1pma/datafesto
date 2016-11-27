from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import include, url
from polls import views as polls_views


urlpatterns = [
    # Examples:
    url(r'^$', polls_views.SaveData.as_view(), name='send_message'),
    url(r'^home.html', polls_views.HomePage.as_view(), name='home_view'),
    url(r'^polls/', include("polls.urls")),
]