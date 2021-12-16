from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic.list import ListView
# Create your views here.
from .models import Item
import datetime
import pandas as pd


def item_list(request):
    if request.method == 'POST':
        data = request.POST
        data = Item.objects.filter(
            Q(shop=data['shop'], department=data['department'], expire_date__lte=datetime.date.today()) |
            Q(quantity=0, shop=data['shop'], department=data['department']))
        value = data.values()
        key = []
        for i in value:
            if i.keys() not in key:
                key.append(i.keys())

    return render(request, "products/item_list.html", {'value':value,})


def search_products(request):
    if request.method == 'GET':
        return render(request, "products/search.html")

    if request.method == 'POST':
        data = request.POST
        data_form = (dict(data.lists()))
        search_item = []
        value = []
        print(data_form)
        if data_form['date'] != ['']:
            search_item.append(Item.objects.filter(expire_date=data["date"]))
        elif data_form['barcode'] != ['']:
            search_item.append(Item.objects.filter(barcode=data["barcode"]))
        elif data_form['CO_code'] != ['']:
            search_item.append(Item.objects.filter(CO_code=data["CO_code"]))
        else:
            raise ValueError("Введіть критерій пошуку")
        for i in search_item:
            value.append(i.values())
        print(search_item)
    return render(request, "products/item_list.html", {'value':value[0],})


def add_products(request):
    if request.method == 'GET':
        return render(request, "products/add_new.html")

    if request.method == 'POST':
        data = request.POST
        data_form = (dict(data))
        new_dict = {}
        for key, value in zip(data_form, data_form.values()):
            value = str(value)[2:-2]
            new_dict[key] = value

        if (data_form['date'] != ['']) and (data_form['barcode'] != ['']) and (data_form['CO_code']) and (data_form['shop'] != ['']) \
                and (data_form['department'] != [''] and (data_form['name'] != [''])):
            new_item = Item.objects.create(name=new_dict['name'], barcode=new_dict['barcode'], expire_date=new_dict['date'], shop=new_dict['shop'],
                                           department=new_dict['department'], CO_code=new_dict['CO_code'])

        else:
            raise ValueError("Заповніть всі поля!")

    return render(request, "products/add_new.html")



def patch_new_date(request):
    if request.method == 'POST':
        data = request.POST
        data = (dict(data.lists()))
        #update date in db
        if data['CO_code']:
            for item, date, qt in zip(data["CO_code"], data['date'], data['quantity']):
                #get item from db
                co = Item.objects.get(CO_code=item)
                # change income date to datetime format
                cd = pd.to_datetime(date).date()
                if cd > datetime.date.today():
                    co.expire_date = cd
                    co.save()
                    if qt == '':
                        co.quantity = 1
                        co.save()
                    else:
                        co.quantity = qt
                        co.save()
                elif qt == '0':
                    co.quantity = qt
                    co.save()
                else:
                    raise ValueError("Введіть коректну дату чи поставте кількість 0")
        else:
            raise ValueError("Введіть дату!")

    return redirect('start_list')


class StartList(ListView):
    model = Item
    template_name = "products/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_shop = Item.objects.values_list("shop")
        shop =[]
        for item in data_shop:
            item = str(item)[2:-3]
            if item not in shop:
                shop.append(item)
            else:
                continue
        context['shop'] = shop
        data_department = Item.objects.values_list("department")
        department = []
        for item in data_department:
            item = str(item)[2:-3]
            if item not in department:
                department.append(item)
            else:
                continue
        context['department'] = department
        return context
