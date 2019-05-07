from django.http import HttpResponse
from . models import Question
from django.template import loader
from django.shortcuts import render,get_objects_or_404
from django.http import Http404

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={
        'latest_question_list':latest_question_list,
        }
    return (request, 'polls/index.html', context)

def detail(request,question_id):
    question =get_objects_or_404(Question,pk=question_id)
    return render(request ,'polls/detail.html',{'question':question})


def results(request,question_id):
    response="you're looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you're voting on question %s" %question_id)
