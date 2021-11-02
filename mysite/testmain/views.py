from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect


from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("안녕하세요 test main에 오신것을 환영합니다.")
    # return redirect(request, 'http://127.0.0.1:8000/pybo/')
    # return render(request, 'testmain/maintemp.html')