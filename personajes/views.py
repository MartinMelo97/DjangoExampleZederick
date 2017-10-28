from django.shortcuts import render
from django.views.generic import View

class PersonajesView(View):
	def get(self,request):
		template_personajes='personajes.html'
		contexto= {'personajes':['Mario,','Luigi y','Peach']}
		return render(request, template_personajes, contexto)
