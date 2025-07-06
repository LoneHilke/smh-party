from django.urls import path
from . import views
from .views import Forside, Ideer,Om,Siger, Bestil, Pris

urlpatterns = [
  path('', Forside.as_view(), name='forside'),
  path('ideer', Ideer.as_view(), name='ideer'),
  path('om', Om.as_view(), name='om'),
  path('siger', Siger.as_view(), name='siger'),
  path('bestil', Bestil.as_view(), name='bestil'),
  path('pris', Pris.as_view(), name='pris'),
]