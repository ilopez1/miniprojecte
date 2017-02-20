# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
import datetime
import sys

@login_required
def fer_backups(request):
    if (request.user.username != "admin"):
        messages.add_message(request, messages.ERROR, 'No tens permisos per fer aquesta acció')
        return HttpResponseRedirect(reverse('videos:llista_videos'))
    else:
        sysout = sys.stdout
        nomFitxer = "backup/media/bdd-Backup" + str(datetime.datetime.now()).replace(" ","").replace(":","-")+".xml"
        sys.stdout = open (nomFitxer, 'w')
        call_command('dumpdata',indent=2,format='xml')
        sys.stdout = sysout
        messages.add_message(request, messages.SUCCESS, 'El backup de la BDD ha sigut creat amb èxit')
        return HttpResponseRedirect(reverse('videos:llista_videos'))
