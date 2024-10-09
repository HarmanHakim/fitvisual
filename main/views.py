from django.shortcuts import render, redirect, get_object_or_404
from main.forms import TokoEntryForm
from main.models import TokoEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP D',
        'npm': '2306123456',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_toko_entry(request):
    form = TokoEntryForm(request.POST or None, request.FILES or None)

    if form.is_valid() and request.method == "POST":
        toko_entry = form.save(commit=False)
        toko_entry.user = request.user
        toko_entry.save()
        return redirect('main:show_main')
    
    else:
        messages.error(request, "Invalid username or password. Please try again.")


    context = {'form': form}
    return render(request, "create_toko_entry.html", context)

@login_required(login_url='/login')
def edit_toko(request, id):
    toko_entry = get_object_or_404(TokoEntry, pk=id)
    if request.method == "POST":
        form = TokoEntryForm(request.POST, instance=toko_entry)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = TokoEntryForm(instance=toko_entry)
    context = {'form': form}
    return render(request, 'edit_toko.html', context)

@login_required(login_url='/login')
def delete_toko(request, id):
    toko_entry = get_object_or_404(TokoEntry, pk=id)
    if request.method == "POST":
        toko_entry.delete()
        return redirect('main:show_main')
    context = {'toko_entry': toko_entry}
    return render(request, 'delete_toko.html', context)

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    nama = strip_tags(request.POST.get("nama"))
    harga = strip_tags(request.POST.get("harga"))
    description = strip_tags(request.POST.get("description"))
    image_url = strip_tags(request.POST.get("image_url"))

    print(nama, harga, description, image_url)

    new_product = TokoEntry(
        nama=nama,
        harga=harga,
        description=description,
        image_url=image_url,
        user=request.user,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)