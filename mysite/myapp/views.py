#views.py
from django.shortcuts import render, redirect
from myapp.models import Member, Member1
 
# Create your views here.
 
def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)

def login(request):
    
    return render(request, 'login.html', context)

def contact(request):
    return render(request, 'contact.html', {})


def orders(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'orders.html', context)

def views(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'views.html', context)

def changeorder(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'changeorder.html', context)

def cancelorder(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'cancelorder.html', context)

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'], item=request.POST['item'], address = request.POST['Deliveryaddress'])
    member.save()
    return redirect('/')
 
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)
 
def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.item = request.POST['item']
    
    member.save()
    return redirect('/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/')
