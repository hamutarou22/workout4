from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Event, Content
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def signupfunc(request):

    if  request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています'})

    return render(request, 'signup.html', {})


def loginfunc(request):
    
    if  request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'not loggedin'})
    return render(request, 'login.html', {'error':'GET'})

@login_required
def index(request):

    if request.POST.get("input")=="1":
       a = request.POST.get("delete_pk")
       print(a)
       object_list = Content.objects.filter(id = request.POST.get("delete_pk")).delete()
       object_list = Content.objects.order_by('-training_date')[:10]
       return render(request, 'index.html', {'object_list':object_list})


    object_list = Content.objects.order_by('-training_date')[:10]
    return render(request, 'index.html', {'object_list':object_list})

@login_required
def neweventfunc(request):
    object_list = Event.objects.all
    return render(request, 'new_event.html', {'object_list':object_list})

@login_required
def neweventfunc2(request):
    if request.POST.get("add")=="1":
        event = request.POST.get("newevent")
        b = Event(event_name = event)
        b.save()
    
    if request.POST.get("delete")=="1":
       instance =  Event.objects.get(id=request.POST.get("delete_pk"))
       instance.delete()
    
    object_list = Event.objects.all
    return render(request, 'new_event.html', {'object_list':object_list})

@login_required
def recordfunc(request):
    if request.POST.get("input")=="1":
        event1 = request.POST.get("Event2")
        weight1 = request.POST.get("weight")
        setnumber1 = request.POST.get("setnumber2")
        b = Content(event=event1, weight=weight1, set_number=setnumber1)
        b.save()
        object_list = Content.objects.order_by('-training_date')
        return render(request, 'index.html', {'object_list':object_list})

    object_list = Event.objects.all
    return render(request, 'record.html', {'object_list':object_list})

def changefunc(request):
    response = "Hello, world. You're at the change."
    return HttpResponse(response)


@login_required
def tablefunc(request):

    if  request.POST.get("input")=="1":
        input2 = "2"
        NumberOfRecord = request.POST.get("number_record")
        result_list = Content.objects.filter(event=request.POST.get("Event2")).order_by('-training_date')[:int(NumberOfRecord)]
        event_list = Event.objects.all
        return render(request, 'make_table.html', {'result_list':result_list, 'event_list':event_list ,"input2":input2 }) 

    else:
        input2 = "1"
        result_list = Content.objects.order_by('-training_date')
        event_list = Event.objects.all
        return render(request, 'make_table.html', {'result_list':result_list, 'event_list':event_list ,"input2":input2 })

def logoutfunc(request):
    logout(request)
    return redirect('login')
