# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    wins = models.IntegerField(default = 0)
    losses = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

class Player (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name="players")
    nfl_team = models.CharField(max_length=255)
    points = models.IntegerField(default = 0)
    touchdowns = models.IntegerField(default = 0)
    bye = models.IntegerField(default = 5)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)