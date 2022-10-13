from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse, HttpRequest
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'username': request.user.username,
        'last_login': request.COOKIES['last_login'],
        'tasks': tasks,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    context = {}
    if request.method == "POST":
        temp = Task(user=request.user, title=request.POST.get('title'), description=request.POST.get('description'))
        temp.save()
        return redirect('todolist:show_todolist')
    return render(request, "create-task.html",context)

@csrf_exempt
@login_required(login_url="/todolist/login/")
def add_task(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        temp = Task.objects.create(
            title=title, description=description, user=request.user
        )
        return JsonResponse({
            "title": title,
            "date": temp.date,
            "description": description
        }, status=200)
    


def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def delete_task(request, id):
    task = Task.objects.filter(pk=id)
    task.delete()
    return redirect('todolist:show_todolist')

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Task.objects.filter(user=request.user)
    
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

