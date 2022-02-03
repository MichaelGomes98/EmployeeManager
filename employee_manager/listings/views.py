from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Employee
from listings.forms import Add

# Create your views here.
#logique pour récupérer les données correctes de la base de données, et les injecter dans la page.
def hello(request):
    employees = Employee.objects.all()
    return render(request, 'listings/hello.html',  {'employees': employees})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>TEST!</p>')

def addUser(request):
    form = Add()
    return render(request, 'listings/addUser.html', {'form': form})   

def updateUser(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    return render(request, 'listings/updateUser.html', {'emp':emp}) 

def insert_data(request):
    employees = Employee.objects.all()
    if request.method == 'POST' :
        name = request.POST['name']
        surname = request.POST['surname']
        departement = request.POST['departement']
        new = Employee(name=name, surname=surname,departement=departement)
        new.save()        
        return render(request, 'listings/hello.html',  {'employees': employees})
    else:
        render(request, "listing/hello.html")

def delete(request, emp_id):
    employees = Employee.objects.all()
    emp = Employee.objects.get(id=emp_id)    
    emp.delete()
    return render(request, 'listings/hello.html',  {'employees': employees})