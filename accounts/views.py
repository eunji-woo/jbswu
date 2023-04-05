from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
import re
from django.utils.safestring import mark_safe
from .models import Profile
from accounts.forms import UserForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import PasswordChangeForm



def home(request):
    return render(
        request,
        'home.html',
    )

def signup(request):
    if request.method == "POST":
        # print(a)  # 로깅 테스트용 오류
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password, email=email)  # 사용자 인증
            profile = Profile(user=user, score1=0, score2=0, score3=0, score4=0, score5=0, score6=0, score7=0, score8=0, score9=0) #, score10=0, score11=0, score12=0)
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})


def editinfo(request):
    res_data = {}
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if len(request.POST['password1']) < 8 or len(request.POST['password1']) >21 or not re.findall('[0-9]', request.POST['password1']) or not re.findall('[a-z]', request.POST['password1']) or not re.findall('[A-Z]', request.POST['password1']) or not re.findall("['~!@#$%^&*(),<.>/?]+", request.POST['password1']) or not re.findall("['~!@#$%^&*(),<.>/?]+", request.POST['password1']):
            res_data['error'] = "비밀번호는 대소문자, 숫자, 특수문자를 모두 포함하여 8글자 이상이어야 합니다."
        elif form.is_valid():
            form.save()
            user = request.user
            user.set_password(request.POST['password1'])
            user.save()
            auth.login(request, user)
            return redirect('/')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'registration/editinfo.html', res_data)




# 회원정보 수정
# def editinfo(request):
#     res_data = {}
#     if request.method == 'POST':
#         if request.user.username != request.POST['username'] and User.objects.filter(username=request.POST['username']).exists():
#             res_data['error'] = '이미 사용 중인 아이디입니다.'
#         elif len(request.POST['password']) < 8 or len(request.POST['password']) >21 and not re.findall('[0-9]', request.POST['password']) and not re.find('[a-z]', request.POST['password']) or not re.findall('[A-Z]', request.POST['password']):
#             res_data['error'] = "비밀번호는 대소문자와 숫자를 모두 포함하여 8글자 이상이어야 합니다."
#         elif request.POST['confirm'] == "" or request.POST['confirm'] != request.POST['password']:
#             res_data['error'] = '비밀번호를 확인하세요.'
#         elif request.POST['password'] == "":
#             res_data['error'] = '비밀번호를 입력하세요.'
#         elif request.POST['email'] == "":
#             res_data['error'] = '이메일을 입력하세요.'
#         elif request.POST['username'] == "":
#             res_data['error'] = '아이디를 입력하세요.'
#         elif request.POST['password'] == request.POST['confirm'] and request.POST['email'] != "" and request.POST['password'] != "" and request.POST['username'] != "":
            # user = request.user
            # user.username = request.POST['username']
            # user.email = request.POST['email']
            # user.set_password(request.POST['password'])
            # user.save()
#             auth.login(request, user)
#             return redirect('/', mark_safe(user.username))
#     return render(request, 'registration/editinfo.html', res_data)


# score 바꾸는법
# def editinfo(request):
#     res_data = {}
#     if request.method == 'POST':
            # user = request.user
            # profile = request.user.profile
            # profile.score1 = "1"
            # profile.save()
#             auth.login(request, user)
#             return redirect('/', mark_safe(user.username))
#     return render(request, 'registration/editinfo.html', res_data)