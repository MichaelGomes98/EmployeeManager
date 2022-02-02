from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Employee

# Create your views here.
def hello(request):
    employees = Employee.objects.all()
    return HttpResponse(f"""<h1>Hello Django!</h1>
            <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{employees[0].name}</li>
        </ul>""")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>TEST!</p>')

def liste(request):
    return HttpResponse('<h1>Liste des employés</h1> <p>Eh oui garcon</p>')      