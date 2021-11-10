from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

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




