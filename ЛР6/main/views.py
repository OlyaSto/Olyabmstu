from django.shortcuts import render
from .models import Rases
from .models import Cans
from rest_framework import viewsets
from .serializers import StockSerializer


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


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Rases.objects.all().order_by('id')
    serializer_class = StockSerializer  # Сериализатор для модели


