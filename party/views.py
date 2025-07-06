from django.shortcuts import render, redirect
from django.views import View

class Forside(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/forside.html')
    
class Ideer(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/ideer.html')
    
class Om(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/om.html')

class Pris(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/pris.html')
    
class Siger(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/siger.html')
    
class Bestil(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'party/bestil.html')