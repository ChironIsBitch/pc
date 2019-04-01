from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from users.models import *
import datetime
from . import forms




# Create your views here.


class Index(View):
    def get(self, request):
        start = Start.objects.all()
        now = datetime.datetime.now()
        zuoyou = datetime.timedelta(minutes=30)
        now = now-zuoyou
        print("1111", now)
        start = start.filter(start_time__gte=now)
        chufa = request.GET.get('start')
        arrival = request.GET.get('arrival')
        s_time = request.GET.get("s_time")
        #从后台获取用户表单到前端
        user_form = Start.objects.get(pk=2)
        print(user_form)

        form = forms.CarForm(instance=user_form)
        print(forms.CarForm,'bbbbbbbbbbbbbbbbbbbbbbbb')


        if chufa:
            if chufa == 'ys':
                start = start.filter(start_choices='ys', start_time__gte=now)
            elif chufa == 'qy':
                start = Start.objects.filter(start_choices='qy', start_time__gte=now)
            elif chufa == 'gz':
                start = Start.objects.filter(start_choices='gz', start_time__gte=now)
        if arrival:
            if arrival == 'ys':
                start = start.filter(end_choices='ys', start_time__gte=now)
            elif arrival == 'qy':
                start = start.filter(end_choices='qy', start_time__gte=now)
            elif arrival == 'gz':
                start = start.filter(end_choices='gz', start_time__gte=now)

        if s_time:
            jintian = int(now.strftime("%d"))
            delta = datetime.timedelta(days=1)
            delta1 = datetime.timedelta(days=2)
            mingtian = now + delta
            mingtian = int(mingtian.strftime("%d"))
            houtian = now + delta1
            houtian = int(houtian.strftime("%d"))
            if s_time == "today":
                start = start.filter(start_time__day=jintian)
                start = start.order_by("start_time")
            elif s_time == "tomorrow":
                start = start.filter(start_time__day=mingtian)
                start = start.order_by("start_time")

            elif s_time == "after":
                start = start.filter(start_time__day=houtian)
                start = start.order_by("start_time")
        # start = start.filter(start_time__day=25)
        return render(request, 'index.html', {
            'start': start,
            'chufa': chufa,
            'arrival': arrival,
            's_time': s_time,
            'form':form,

        })
    def post(self, request):
        shili = Start.objects.get(pk=2)
        # print(request.POST, 'zzzzzzzzz')
        form1 = forms.CarForm(request.POST, instance=shili)
        form1.save()
        return HttpResponse('成功')

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)
        print(user_name, pass_word)
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {
                'user': user
            })
        else:

            return HttpResponse('false')
    else:
        return render(request, 'index.html')


def users_logout(request):
    logout(request)


def register_from(request):
    if request.method == 'POST':
        r_username = request.POST.get('r_username')
        r_password = request.POST.get('r_password')
        r_nickname = request.POST.get('r_nickname')
        r_num = request.POST.get('r_num')
        # r_pic = request.FILES.get('pic')

        print(r_nickname, r_num, r_username, r_password)
        if UserProfile.objects.filter(username=r_username):
            print('用户已存在')
            return HttpResponse("1")
        user_profile = UserProfile()
        user_profile.username = r_username
        user_profile.password = make_password(r_password)
        user_profile.nick_name = r_nickname
        user_profile.mobile = r_num

        user_profile.save()
        return HttpResponse("2")

        print(r_username, r_password)
        return render(request, 'index.html')
