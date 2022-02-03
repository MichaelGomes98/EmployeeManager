from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Employee

# Create your views here.
#logique pour récupérer les données correctes de la base de données, et les injecter dans la page.
def hello(request):
    employees = Employee.objects.all()
    return render(request, 'listings/hello.html',  {'employees': employees})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>TEST!</p>')

def liste(request):
    return HttpResponse('<h1>Liste des employés</h1> <p>Eh oui garcon</p>')      