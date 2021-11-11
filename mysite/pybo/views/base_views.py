from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Question

def index(request): #return  render를 통해 question_list.html을 필요한 내용을 주고 render
    #request는 장고에서 자동으로 전달되는 http요청 객체이다.
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page',1) # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so','recent') # 정렬기준

    question_list = Question.objects.order_by('-create_date')

    # question_list = Question.objects.order_by('-create_date')
    # context = {'question_list': question_list} #페이징 처리 하기전
    if kw:
        question_list = question_list.filter(
            # ※ subject__contains=kw 대신 subject__icontains=kw을 사용하면 대소문자를 가리지 않고 찾아 준다.
            Q(subject__icontains=kw) |  # 제목에 kw 포함되어있는지 확인 
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw)  # 질문 글쓴이검색 #모델 속성에 접근하기 위해서 언더바 2개
        ).distinct()

    # 페이징 처리리
    paginator = Paginator(question_list, 10) #페이지당 10개
    page_obj = paginator.get_page(page) #paginator를 이용하여 요청된 페이지에 해당되는 page_obj 를 생성
    # https://wikidocs.net/71240 page_obj에 다양한 속성들 있음
    context = {'question_list':page_obj, 'page': page, 'kw': kw, 'so':so}

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id): #호출 시 render를 통해 question_detail.html render
    """
    pybo 상세내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)




