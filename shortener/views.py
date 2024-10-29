import string
import random

from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import Redirect

# Create your views here.
def home(request):
    return render(request, 'shortener/home.html')

def save(request):
    url = request.POST['url']
    shortcut = request.POST['shortcut']
    if shortcut == '':
        while Redirect.objects.filter(shortHand = shortcut) or shortcut =='': # generate random key and check that it isn't already being used. 
            shortcut = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    if Redirect.objects.filter(shortHand = shortcut): # if shortcut already exists in database
        messages.error(request, 'That new url name is already being used. Please choose another new url name.')
    elif url == '':
        messages.error(request, 'Please make sure that you have input a url to be redirected to.')
    else:
        entry = Redirect(url = url, shortHand = shortcut)
        entry.save()
        messages.success(request, f'Success! You can now navigate to {entry.url} by typing localhost:8000/{entry.shortHand} into your search bar.')

    return HttpResponseRedirect(request.META["HTTP_REFERER"])

def deflect(request, url_id):
    entry = get_object_or_404(Redirect, shortHand = url_id)
    return redirect(entry.url)