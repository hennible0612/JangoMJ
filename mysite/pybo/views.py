from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator #목록이 너무 많아 페이지 사용시 사용
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request): #return  render를 통해 question_list.html을 필요한 내용을 주고 render
    #request는 장고에서 자동으로 전달되는 http요청 객체이다.
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page',1) # 페이지

    question_list = Question.objects.order_by('-create_date')
    # context = {'question_list': question_list} #페이징 처리 하기전

    # 페이징 처리리
    paginator = Paginator(question_list, 10) #페이지당 10개
    page_obj = paginator.get_page(page) #paginator를 이용하여 요청된 페이지에 해당되는 page_obj 를 생성
    # https://wikidocs.net/71240 page_obj에 다양한 속성들 있음
    context = {'question_list':page_obj}

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id): #호출 시 render를 통해 question_detail.html render
    """
    pybo 상세내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login') #로그인이 안되어있으면 자동으로 로그인 화면으로이동
def answer_create(request, question_id): #호출시 answer을 Post을 통해 가져오고 rediredct로 pybo에 detail 호출
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now()) #답변은 request.post.get으로 가지고온다
    # answer.save()
    # return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login') #로그인이 안되어있으면 자동으로 로그인 화면으로이동
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':#저장하기가 post방식인 이유는 form 태그에서 action 속성이 지정되지 않으면 현재 페이지가 디폴트 action으로 설정되기 때문이다.
        #그러므로 question_create함수가 실행이 되고 값은 post가 되어 if문에서 걸린다.
        form = QuestionForm(request.POST) #request.POST 인수로 줄시 subject, content값이 QuestionForm의 subject, content 속성에 자동으로 저장되어 객체가됨
        if form.is_valid(): #form 비어있는지 check
            question = form.save(commit=False) #임시저장
            question.create_date = timezone.now()
            question.save() #실제저장
            return redirect('pybo:index')
    else:
        form = QuestionForm() #메인화면에서 질문등록하기 누르면 get 방식이므로 else로 빠지고 질문등록하기 form을 render
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')