# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^fer_backups/$', views.fer_backups, name='fer_backups'),
]