from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Lists, Sentences, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as User_dj
from django.db import connection
# Create your views here.


def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('alo')
            return redirect('word_lists_words')
        else:
            print('alffffo')
            messages.success(request, ('Không hợp lệ, hãy thử lại...'))
            return redirect('login') #name of a view, not the fuction name
        
    return render(request, 'registration/login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def ajax_word_crud(request):
    if request.method=='GET':
        action=request.GET.get('action')
        if action=='c' or action=='u':
            sentence= request.GET.get('sentence')
            meaning= request.GET.get('meaning')
            note= request.GET.get('note')
            list_id= request.GET.get('list_id')
            choosed_word_tokens_pos = request.GET.getlist("choosed_word_tokens_pos[]")
            tokens=sentence.split()
            lemma=' '.join([tokens[i] for i in range(int(choosed_word_tokens_pos[0]), int(choosed_word_tokens_pos[-1])+1)])
            if action=='c':
                m=Sentences(
                    sentence=sentence, 
                    meaning=meaning, 
                    lemma=lemma,
                    note=note, 
                    word_start_pos=choosed_word_tokens_pos[0], 
                    word_end_pos=choosed_word_tokens_pos[-1], 
                    list_id=list_id,
                    )
                m.save()
                return JsonResponse({"status": 'success'})
            elif action=='u':
                sentence_id= request.GET.get('sentence_id')
                Sentences.objects.filter(sentence_id=sentence_id).update(sentence=sentence, 
                                                                            meaning=meaning, 
                                                                            lemma=lemma,
                                                                            note=note, 
                                                                            word_start_pos=choosed_word_tokens_pos[0], 
                                                                            word_end_pos=choosed_word_tokens_pos[-1], 
                                                                            list_id=list_id)
                return JsonResponse({"status": 'success'})
        elif action=='d':
            sentence_id=request.GET.get('sentence_id')
            Sentences.objects.filter(sentence_id=sentence_id).delete()
            return JsonResponse({"status": 'success'})
       

def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]


@login_required
def show_list_word(request):
    cur_user=request.user.id

    with connection.cursor() as c:
        c.execute("""select * from sentences s  where s.list_id in 
                    (
                        select list_id from lists l where l.user_id=%s
                    )
                  """, [cur_user])
        rows=dictfetchall(c)
        
    return render(request, 'show_list_word.html', {
        'lists': Lists.objects.filter(user_id=cur_user),
        'sents': rows
        })

@login_required
def ajax_crud_list(request):
    if request.method=='GET':
        action=request.GET.get('action')
        if action=='c':
            listname=request.GET.get('listname')
            m=Lists(listname=listname, user_id=request.user.id)
            m.save()
            return JsonResponse({"status": 'success'})
        elif action=='d':
            list_id=request.GET.get('list_id')
            Lists.objects.filter(list_id=list_id).delete()
            return JsonResponse({"status": 'success'})
        elif action=='u':
            list_id=request.GET.get('list_id')
            listname=request.GET.get('listname')
            Lists.objects.filter(list_id=list_id).update(listname=listname)
            return JsonResponse({"status": 'success'})