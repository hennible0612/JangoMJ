from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, Http404, get_object_or_404
from .models import Question

#request 는 클라이언트에서 받음
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list, }#context에 html 에 넣을 데이터 정리
    return render(request,'polls/index.html', context) #context와 넘겨줌

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)


