from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Create your views here.

from .models import Question


def index(request):
    question_list =\
         Question.objects.order_by('-pub_date')
    return render(request,'question_list.html',{'question_list' : question_list})
    
    #result = [ q.subject for q in question_list ]
    #return JsonResponse(result ,safe=False)
    #return HttpResponse( str(result) )

def detail(request,question_id) :
    question=Question.objects.get(pk=question_id)
    return render(request,'question_detail.html',{'question':question})

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(
    content=request.POST.get('content'), create_date=timezone.now())
    return redirect('polls:detail', question_id=question.id)


'''
def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
    'question': question
    }
    return render(
    request, 'question_detail.html', context)
    '''