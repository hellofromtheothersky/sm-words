from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Lists, Sentences, Users
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as User_dj
# Create your views here.


def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_word')
        else:
            messages.success(request, ('Không hợp lệ, hãy thử lại...'))
            return redirect('login') #name of a view, not the fuction name
        
    return render(request, 'registration/login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def add_word(request):
    cur_user=request.user.id
    return render(request, 'add_word.html', {'lists': Lists.objects.filter(user_id=cur_user)})


@login_required
def ajax_add_word(request):
    if request.method=='GET':
        sentence= request.GET.get('sentence')
        meaning= request.GET.get('meaning')
        note= request.GET.get('note')
        list_id= request.GET.get('list_id')
        wordidx = request.GET.getlist("wordidx[]")
        m=Sentences(
            sentences=sentence, 
            meaning=meaning, 
            note=note, 
            word_start_pos=wordidx[0], 
            word_end_pos=wordidx[-1], 
            list_id=list_id
            )
        m.save()
        return JsonResponse({"status": 'success'})
    
    
@login_required
def show_list(request):
    return render(request, 'show_list.html')