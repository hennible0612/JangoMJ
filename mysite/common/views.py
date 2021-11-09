from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
# Create your views here.
def signup(request):
    """
    계정생성
    """
    if request.method == "POST": #만약 POST이면 계정생성화면을 리턴
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #사용자가 사용자명과 비밀번호를 정확하게 입력했는지 확인
            login(request, user) #회원가입 할시 자동으로 로그인
            return redirect('index')
    else: #get 인 경우에는 입력한 데이터로 사용자를 생성
        form = UserForm()
    return render(request,'common/signup.html', {'form': form})