from django.shortcuts import render,redirect
from .models import Emloyees
from .models import Service
# Create your views here.

#insert into database
def insert(request):
    if request.method=="POST":
        nom=request.POST['nom']
        email=request.POST['email']
        id_service=request.POST['id_service']
        emp=Emloyees(nom=nom,email=email,service_id=id_service)
        emp.save()
        return redirect('/')
      
    services=Service.objects.all()
    return render(request,"index.html",{'services':services})

#List data from database
def view(request):
    emloyees=Emloyees.objects.select_related('service')
    return render(request,'view.html',{'employees':emloyees})
def delete(request,id):
    emp=Emloyees.objects.get(id=id)
    emp.delete()
    return redirect('/')
def edit(request,id):
    emp_edit=Emloyees.objects.get(id=id)
    services=Service.objects.all()
    return render(request,'edit.html',{'emp_edit':emp_edit,'services':services})
def update(request):
    id=request.POST['id']
    nom=request.POST['nom']
    email=request.POST['email']
    id_service=request.POST['id_service']
    emp = Emloyees.objects.get(id=id)
    emp.nom = nom
    emp.email = email
    emp.service_id = id_service
    emp.save()
    return redirect('/')
