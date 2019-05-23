from django.shortcuts import render
from django.http import HttpResponse
import uuid
from django.db import transaction
from core.models import Player

# Create your views here.
def getCash(request):
    cash = Player.CASH_LIST
    links = {
        '10': 'https://en.numista.com/catalogue/photos/hong_kong/g557.jpg',
        '5': 'https://s3.amazonaws.com/ngccoin-production/world-coin-price-guide/107250b.jpg',
        '2': 'https://s3.amazonaws.com/ngccoin-production/world-coin-price-guide/107218b.jpg',
        '1': 'https://www.leftovercurrency.com/wp-content/uploads/2017/04/1-hong-kong-dollar-coin-obverse-1.jpg',
        '0.5': 'https://cdn.shopify.com/s/files/1/0938/5674/products/6f9e6bba10a74eba00cab925539d9883_1024x1024.jpg?v=1500056645',
        '0.2': 'https://d1w8cc2yygc27j.cloudfront.net/3529093949651229227/6177759791735850913.jpg',
        '0.1': 'https://cdn.shopify.com/s/files/1/0938/5674/products/d9c45143227326a5462f0ecc315be7a8_large.jpg?v=1536883686'

    }
    try:
        request.session['id']
    except KeyError:
        request.session['id'] = str(uuid.uuid4())
        index = None
        with transaction.atomic():
            player = Player.objects.select_for_update().first()
            player.cash = (player.cash + 1) % 7
            index = player.cash - 1
            request.session['cash'] = cash[index]
            player.save()
    style = '<style>.bg {background-image: url("'+links[str(request.session['cash'])]+'");height:100vh;background-position: center;background-repeat: no-repeat;background-size: cover;}</style>'
    return HttpResponse(style + '<div class="bg"></div>')