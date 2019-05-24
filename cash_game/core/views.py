from django.shortcuts import render
from django.http import HttpResponse
import uuid
from django.db import transaction
from core.models import Player

# Create your views here.
def getCash(request):
    cash = Player.CASH_LIST
    links = Player.LINKS
    try:
        request.session['id']
    except KeyError:
        request.session['id'] = str(uuid.uuid4())
        index = None
        with transaction.atomic():
            player = Player.objects.select_for_update().first()
            player.cash = (player.cash + 1) % len(links)
            index = player.cash - 1
            request.session['cash'] = cash[index]
            player.save()
    style = '<style>.bg {background-image: url("'+links[str(request.session['cash'])]+'");height:100vh;background-position: center;background-repeat: no-repeat;background-size: cover;}</style>'
    return HttpResponse(style + '<div class="bg"></div>')