from django.shortcuts import render
from django.views.generic import View

class NivelesView(View):
	def get(self,request):
		template_niveles='niveles.html'
		contexto= {'niveles':['1','2','3','4']}
		return render(request, template_niveles, contexto)
