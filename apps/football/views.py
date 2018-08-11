# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    context = {
        "my_players": Player.objects.filter(owner = User.objects.get(id=2)),
        "my_rbs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "running back"),
        "my_wrs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "wide receiver"),
        "my_qbs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "quarterback"),
        "my_tes": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "tight end"),



    }
    return render(request, 'football/index.html', context)
def players(request):
    context = {
        "players" : Player.objects.all(),
        "users" : User.objects.all()
    }
    return render(request, 'football/players.html', context)
