from django.shortcuts import render, redirect
from main.forms import TokoEntryForm
from main.models import TokoEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    toko_entries = TokoEntry.objects.all()
    context = {
        'npm' : '2306240080',
        'name': 'Harman Hakim',
        'class': 'PBP A',
        'toko_entries': toko_entries,
    }

    return render(request, "main.html", context)

def create_toko_entry(request):
    form = TokoEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_toko_entry.html", context)

def show_xml(request):
    data = TokoEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = TokoEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = TokoEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = TokoEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")