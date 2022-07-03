from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import WarehouseAccess


def index(request):
    warehouse_users = WarehouseAccess.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'warehouse_users': warehouse_users,
    }
    return HttpResponse(template.render(context, request))



def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['password']
    warehouseman = WarehouseAccess(firstname=x, lastname=y, password=z)
    warehouseman.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    warehouse_users = WarehouseAccess.objects.get(id=id)
    warehouse_users.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
  warehouse_users = WarehouseAccess.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'warehouse_users': warehouse_users,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  password = request.POST['password']
  warehouse_users = WarehouseAccess.objects.get(id=id)
  warehouse_users.firstname = first
  warehouse_users.lastname = last
  warehouse_users.password = password
  warehouse_users.save()
  return HttpResponseRedirect(reverse('index'))