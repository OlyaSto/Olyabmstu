from django.http import HttpResponse
from django.shortcuts import render
from .models import Creat


def master(request):
    crs = {'crs': Creat.objects.order_by('id')}
    return render(request, 'master/list.html', crs)


def detail(request, cr_id):
    cr = Creat.objects.get(id=cr_id)
    return render(request, 'master/detail.html', {'cr': cr})

