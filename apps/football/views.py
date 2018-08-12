# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    context = {
        "users": User.objects.exclude(id=1)
    }
    return render(request, 'football/index.html', context)
def team(request):
    context = {
        "my_players": Player.objects.filter(owner = User.objects.get(id=2)),
        "my_rbs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "running back"),
        "my_wrs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "wide receiver"),
        "my_qbs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "quarterback"),
        "my_tes": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "tight end"),
    }
    return render(request, 'football/team.html', context)
def players(request):
    context = {
        "players" : Player.objects.all(),
        "users" : User.objects.all()
    }
    return render(request, 'football/players.html', context)
def teamx(request, user_id):
    print user_id
    context = {
        # switch context to be by id
        "user": User.objects.get(id=user_id),
        "my_players": Player.objects.filter(owner = User.objects.get(id=user_id)),
        "my_rbs": Player.objects.filter(owner = User.objects.get(id=user_id)).filter(position = "running back"),
        "my_wrs": Player.objects.filter(owner = User.objects.get(id=user_id)).filter(position = "wide receiver"),
        "my_qbs": Player.objects.filter(owner = User.objects.get(id=user_id)).filter(position = "quarterback"),
        "my_tes": Player.objects.filter(owner = User.objects.get(id=user_id)).filter(position = "tight end"),
    }
    return render(request, 'football/teamx.html', context)
def qbs(request):
    context = {
        "qbs": Player.objects.filter(position = "quarterback"),
    }
    return render(request, 'football/qbs.html', context)
def rbs(request):
    context = {
        "rbs": Player.objects.filter(position = "running back"),
    }
    return render(request, 'football/rbs.html', context)
def wrs(request):
    context = {
        "wrs": Player.objects.filter(position = "wide receiver"),
    }
    return render(request, 'football/wrs.html', context)
def tes(request):
    context = {
        "tes": Player.objects.filter(position = "tight end"),
    }
    return render(request, 'football/tes.html', context)
def playerx(request, player_id):
    print player_id
    context = {
        "player": Player.objects.get(id=player_id),
    }
    return render(request, 'football/player.html', context)

def odell(request):
    return render(request, 'football/odell.html')