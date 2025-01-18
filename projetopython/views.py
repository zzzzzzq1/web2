from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("A view index funcionou, Wowo!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim<h1>")

def contato(request):
    return HttpResponse("<h1>Pagina de contato<h1>")

def ajuda(request):
    return HttpResponse("<h1>Pagina de ajuda<h1>")
# Create your views here.
