from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contatos(request):
    return render(request,'contatos.html')

def ajuda(request):
    return render(request,'ajuda.html')
# Create your views here.