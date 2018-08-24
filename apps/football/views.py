# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
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

def add(request):
    print "add"
    # PASSWORD PROTECT ADDING PLAYERS
    return render(request, 'football/add.html')

def create(request):
    print "create"
    print request.POST
    print request.POST['first_name']
    print request.POST['last_name']
    Player.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], position=request.POST['position'],nfl_team=request.POST['nfl_team'],rank=request.POST['rank'],summary=request.POST['summary'],identifier=request.POST['identifier'])
    print "working?"
    return redirect('/add')

def edit(request, player_id):
    print "editing"
    print player_id
    my_player = Player.objects.get(id=player_id)
    print my_player.position
    posish = my_player.position
    context = {
        "player": Player.objects.get(id=player_id),
        "posish": posish
    }
    return render(request, 'football/edit.html', context)

def update(request, player_id):
    if request.POST['password']!= "codejoy":
        print "fuck you"
        return redirect('/odell')
    print "updating"
    print player_id
    print request.POST
    x = Player.objects.get(id=player_id)
    x.first_name = request.POST['first_name']
    x.last_name = request.POST['last_name']
    x.position = request.POST['position']
    if x.position == "running":
        print "BINGO runner"
        x.position = "running back"
    if x.position == "wide":
        print "BINGO RECEIVER"
        x.position = "wide receiver"
    if x.position == "tight":
        print "BINGO Tight end"
        x.position = "tight end"

    x.bye = request.POST['bye']
    x.nfl_team = request.POST['nfl_team']
    x.identifier = request.POST['identifier']

    x.summary = request.POST['summary']

    x.rank = request.POST['rank']
    x.touchdowns = request.POST['touchdowns']
    x.points = request.POST['points']
    x.save()
    # get player and then make a variable and make changes and save variable
    return redirect('/player/'+player_id)

def draft(request):
    print "drafting"
    context = {
        "players": Player.objects.all(),
        "undrafted": Player.objects.filter(status="undrafted"),
        "drafted": Player.objects.filter(status="drafted"),
    }
    return render(request, 'football/draft.html', context)

def drafting(request, player_id):
    print "drafting this player"
    print player_id
    x = Player.objects.get(id=player_id)
    x.status = "drafted"
    x.save()
    # get player and then make a variable and make changes and save variable
    return redirect('/draft')

def redraft(request, player_id):
    print "redrafting this player"
    print player_id
    x = Player.objects.get(id=player_id)
    x.status = "undrafted"
    x.save()
    # get player and then make a variable and make changes and save variable
    return redirect('/draft')

def odell(request):
    return render(request, 'football/odell.html')