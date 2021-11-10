
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

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
