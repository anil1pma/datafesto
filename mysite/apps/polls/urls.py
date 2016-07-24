from django.conf.urls import url

from mysite.apps.polls import views

urlpatterns = [
    url(r'^savedata', views.SaveData.as_view(), name='send_message'),
]