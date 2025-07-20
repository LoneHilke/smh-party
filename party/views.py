from django.shortcuts import render, redirect
from django.views import View
from .models import Fest, Anmeld, Mig
from .forms import FestForm, AnmeldForm

class Forside(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/forside.html')
    
"""class Ideer(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/ideer.html')"""
    
class Om(View):
    def get(self, request, *args, **kwargs):
        mig = Mig.objects.all() 
        
        context = {
            'mig': mig,
            
        }       
        return render(request, 'party/om.html', context)

class Pris(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/pris.html')
    
class Siger(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/siger.html')
    
class Bestil(View):
    def get(self, request, *args, **kwargs):
        fest = Fest.objects.all()
        form = FestForm()
        context = {
            'fest': fest,
            'form': form
        }
        return render(request, 'party/bestil.html',context)
    
class Andre(View):
    def get(self, request, *args, **kwargs):
        anmeld = Anmeld.objects.all()
        form = AnmeldForm()
        context = {
            'anmeld': anmeld,
            'form': form
        }
        return render(request, 'party/andre.html', context)