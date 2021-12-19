from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Rases
from .models import Cans
from .forms import RasesForm, CansForm
from django.http import HttpResponse, HttpResponseNotFound


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


def report(request):
    cr = Rases.objects.all()
    c = Cans.objects.all()
    return render(request, 'main/rep.html', {'c': c, 'cr': cr})


def create(request):
    error= ''
    if request.method == 'POST':
        form = RasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('master')
        else:
            error = 'Данные введены некорректно!'

    form = RasesForm()

    data = {
       'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


def update(request, cr_id):
    try:
        cr = Rases.objects.get(id=cr_id)

        if request.method == "POST":
            cr.name = request.POST.get("name")
            cr.discription = request.POST.get("discription")
            cr.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/update.html", {"cr": cr})
    except cr.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete(request, cr_id):
    try:
        cr = Rases.objects.get(id=cr_id)
        cr.delete()
        return HttpResponseRedirect("/")
    except cr.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def create1(request, cr_id):
    cr = Rases.objects.all()
    error = ''
    if request.method == 'POST':
        form = CansForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Данные введены некорректно!'

    form = CansForm()

    data = {
        'form': form,
        'error': error,
        'cr': cr,
    }
    return render(request, 'main/create1.html', data)

def update1(request, cr_id):
    try:
        cr = Cans.objects.get(id=cr_id)
        ras = Rases.objects.all()
        if request.method == "POST":
            cr.idrases = request.POST.get("idrases")
            cr.cans = request.POST.get("cans")
            cr.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/update2.html", {"cr": cr, "c": ras})
    except cr.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def delete1(request, cr_id):
    try:
        cr = Cans.objects.get(id=cr_id)
        cr.delete()
        return HttpResponseRedirect("/")
    except cr.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")