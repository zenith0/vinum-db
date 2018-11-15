from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Wine
from django.contrib.auth.decorators import login_required
    
class WineList(ListView):
    login_required = True
    model = Wine

class WineDetailView(DetailView):
    login_required = True
    model = Wine