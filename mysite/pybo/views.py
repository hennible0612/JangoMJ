from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone

# Create your views here.
def index(request): #return  render를 통해 question_list.html을 필요한 내용을 주고 render
    #request는 장고에서 자동으로 전달되는 http요청 객체이다.
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('create_date')
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id): #호출 시 render를 통해 question_detail.html render
    """
    pybo 상세내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id): #호출시 answer을 Post을 통해 가져오고 rediredct로 pybo에 detail 호출
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now()) #답변은 request.post.get으로 가지고온다
    answer.save()
    return redirect('pybo:detail', question_id=question.id)
