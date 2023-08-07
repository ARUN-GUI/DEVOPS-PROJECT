from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import App
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    members = App.objects.all().values()
    template = loader.get_template('index.html')

    context = {'members':members}
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = App(firstname = x , lastname = y)
    member.save()
    return HttpResponseRedirect(reverse('index'))
def delete(request,id):
    new = App.objects.get(id = id)
    new.delete()
    return HttpResponseRedirect(reverse('index'))

                     


# Create your views here.
