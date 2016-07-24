from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import include, url
from polls import views as polls_views


urlpatterns = [
    # Examples:
    url(r'^$', polls_views.SaveData.as_view(), name='send_message'),
    url(r'^polls/', include("polls.urls")),
    url(r'^admin/', include(admin.site.urls)),
]