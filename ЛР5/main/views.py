from django.shortcuts import render
from .models import Rases
from .models import Cans


def master(request):
    crs = {'crs': Rases.objects.order_by('id')}
    return render(request, 'main/list.html', crs)


def detail(request, cr_id):
    cr = Rases.objects.get(id=cr_id)
    return render(request, 'main/detail.html', {'cr': cr})


def can(request, cr_id):
    cr = Rases.objects.get(id=cr_id)
    c = Cans.objects.all()
    return render(request, 'main/second.html', {'c': c, 'cr': cr})



