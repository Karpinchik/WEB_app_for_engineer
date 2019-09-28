from django.shortcuts import render
from app_to.models import Customers, Obj


def app_start(request):
    data = Customers.objects.all()
    context = {'data': data}
    return render(request, 'app_to/data.html', context)


def list_obj(request, pk):
    data = Customers.objects.all()   # получаю список заказчиков, чтобы из него получить объект по pk
    item_obj = request.GET.get('item', '')           # получаю значение параметра запроса pk
    obj_pk = data.get(id=item_obj)
    iter_obj_pk = obj_pk.cust.all()
    context = {'data': iter_obj_pk}
    print(123)
    return render(request, 'app_to/data_obj.html', context)


def data_obj(request, pk):
    data = Customers.objects.all()   # получаю список заказчиков, чтобы из него получить объект по pk
    item_obj = request.GET.get('item', '')           # получаю значение параметра запроса pk
    obj_pk = data.get(id=item_obj)
    iter_obj_pk = obj_pk.cust.all()
    context = {'data': iter_obj_pk}


    return render(request, 'app_to/data_obj.html', context)

