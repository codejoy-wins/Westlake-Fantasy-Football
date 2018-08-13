from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^team$', views.team),
    url(r'^players$', views.players),
    url(r'^team/(?P<user_id>\d+)$', views.teamx),
    url(r'^qbs$', views.qbs),
    url(r'^rbs$', views.rbs),
    url(r'^wrs$', views.wrs),
    url(r'^tes$', views.tes),
    url(r'^player/(?P<player_id>\d+)$', views.playerx),

    url(r'^', views.odell),
]
