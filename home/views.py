from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Lists, Sentences
# Create your views here.


def add_word(request):
    return render(request, 'add_word.html', {'lists': Lists.objects.all})

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