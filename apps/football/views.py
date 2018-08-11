# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    context = {
        "my_players": Player.objects.filter(owner = User.objects.get(id=2))
    }
    return render(request, 'football/index.html', context)
def players(request):
    context = {
        "players" : Player.objects.all(),
        "users" : User.objects.all()
    }
    return render(request, 'football/players.html', context)
