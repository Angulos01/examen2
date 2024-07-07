from django.shortcuts import render, redirect
from django.views import generic
import requests
from .forms import CreatePendienteForm

class ListPendientesView(generic.View):
    template_name = "home/list_pend.html"
    url = "http://127.0.0.1:8000/api/pendientes/list/"
    
    def get(self, request):
        response = requests.get(url=self.url)
        pendientes = response.json()

        filtro = request.GET.get('filtro', 'todos')

        if filtro == 'todos':
            context = {"pendientes": pendientes, "filtro": filtro}
        elif filtro == 'pendientes_ids':
            context = {"pendientes": [pd for pd in pendientes if pd['state'] == 'PENDIENTE'], "filtro": filtro}
        elif filtro == 'pendientes_ids_titles':
            context = {"pendientes": [pd for pd in pendientes if pd['state'] == 'PENDIENTE'], "filtro": filtro}
        elif filtro == 'pendientes_ids_userid':
            context = {"pendientes": [pd for pd in pendientes if pd['state'] == 'PENDIENTE'], "filtro": filtro}
        elif filtro == 'sin_resolver_ids_titles':
            context = {"pendientes": [pd for pd in pendientes if pd['state'] == 'SIN_RESOLVER'], "filtro": filtro}
        elif filtro == 'sin_resolver_ids_userid':
            context = {"pendientes": [pd for pd in pendientes if pd['state'] == 'SIN_RESOLVER'], "filtro": filtro}
        elif filtro == 'resueltos_ids_titles':
            context = {"pendientes": [pd for pd in pendientes if pd['state'] == 'RESUELTO'], "filtro": filtro}
        elif filtro == 'resueltos_ids_userid':
            context = {"pendientes": [pd for pd in pendientes if pd['state'] == 'RESUELTO'], "filtro": filtro}

        
        return render(request, self.template_name, context)

class CreatePendienteView(generic.View):
    template_name = "home/create_pend.html"
    context = {}
    payload = {}
    url = "http://127.0.0.1:8000/api/pendientes/create/"
    response = None
    form_class = CreatePendienteForm
    def get(self, request):
        self.context = {
            "form": self.form_class,
        }
        return render(request, self.template_name, self.context)

    def post(self, request):
        payload = {
            "title": request.POST["title"],
            "description": request.POST["description"],
            "user": request.user.username,
            "priority": request.POST["priority"],
            "state": request.POST["state"],
            "status": request.POST["status"],
            "user": 1
        }
        self.response = requests.post(url=self.url, data=payload)
        return redirect("home:list_pend")
