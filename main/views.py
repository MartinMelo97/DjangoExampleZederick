from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

def lavista(self):
	sopes= 'sinpollo'
	cantidad= 3
	frase= str(cantidad) + 'sopes'
	return HttpResponse(frase)

class SopesView(View):
	def get(self,request):
		template_name = 'home.html'
		contexto= {'cantidad':3, 'sabor':'sin pollo', 'pollo':True}
		return render(request, template_name, contexto)
