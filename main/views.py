import requests
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response

def index(request):

	STATIC_URL = settings.STATIC_URL

	req = requests.get('https://graph.facebook.com/JustinBieber')
	info = req.json
	info["STATIC_URL"] = settings.STATIC_URL

	return render_to_response('starter-template.html', info)