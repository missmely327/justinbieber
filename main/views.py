import requests
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response

def index(request):

	STATIC_URL = settings.STATIC_URL

	req = requests.get('https://graph.facebook.com/JustinBieber')

	name = req.json["name"]
	cover_source = req.json["cover"]["source"]
	likes = req.json["likes"]

	return render_to_response('starter-template.html', locals())