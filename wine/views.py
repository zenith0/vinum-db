from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Wine

class WineList(ListView):
    model = Wine

class WineDetailView(DetailView):
    model = Wine