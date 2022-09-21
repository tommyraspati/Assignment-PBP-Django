from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_mywatchlist_item = MyWatchListItem.objects.all()
    context = {
        'movie_list': data_mywatchlist_item,
        'nama': 'Raspati Mahatma K.D (Tommy)',
        'id': '2106750244'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_html(request):
    data_mywatchlist_item = MyWatchListItem.objects.all()
    context = {
        'movie_list': data_mywatchlist_item,
        'nama': 'Raspati Mahatma K.D (Tommy)',
        'id': '2106750244'
    }
    return render(request, "mywatchlist.html", context)
