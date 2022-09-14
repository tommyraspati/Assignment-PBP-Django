from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': data_catalog_item,
        'nama': 'Raspati Mahatma K.D (Tommy)',
        'id': '2106750244'
    }
    return render(request, "katalog.html", context)