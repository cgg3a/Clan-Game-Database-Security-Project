import os
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from clan_game.models import *


@csrf_exempt
def sign_in(request):
    context = {
        'google_oauth_client_id': os.environ['GOOGLE_OAUTH_CLIENT_ID']
    }
    return render(request, 'sign_in.html', context=context)

@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )

    except ValueError:
        return HttpResponse(status=403)

    player = Player(user_data["email"], user_data["name"])
    player.save()
    player.get()

    # TODO: 
    #save login activity to database
    # login = Login()

    # save to session data    
    user_data['clanId'] = player.clanId
    user_data['score'] = player.score
    request.session['user_data'] = user_data

    return redirect('sign_in')

def sign_out(request):
    del request.session['user_data']
    return redirect('sign_in')

def profie(request):
    if "user_data" not in request.session:
        return redirect('sign_in')

    return render(request, "dashboard.html")

def clan(request):
    if "user_data" not in request.session:
        return redirect('sign_in')
    clans = Clan.getAllClans()
    context = {
        "clans": clans, 
    }
    get_client_ip(request)
    return render(request, "clan.html", context=context)

def transactions(request):
    if "user_data" not in request.session:
        return redirect('sign_in')

    return render(request, "transactions.html")

def payment(request):
    if "user_data" not in request.session:
        return redirect('sign_in')

    return render(request, "payment.html")

# TODO:
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip