from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from .forms import UserForm,RegisterForm

# Create your views here.
def index(request):
    return render(request,'polls/index.html')


def login(request):
    if request.method == "POST":

        # useremail = request.POST.get('useremail')
        # password = request.POST.get('password')
        # message = "所有字段都必须填写！"
        # if useremail and password:
        #     try:
        #         user = models.User.objects.get(Email=useremail)
        #         if user.password == password:
        #             return redirect('/index/')
        #         else:
        #             message = "密码不正确！"
        #     except:
        #         message = "用户名不存在!"
        # return render(request, 'polls/login.html',{"message":message})
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            useremail = login_form.cleaned_data['useremail']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(Email=useremail)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.Name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'polls/login.html', locals())

    login_form = UserForm()
    return render(request, 'polls/login.html',locals())

def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['Name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['Email']
            nationality = register_form.cleaned_data['Nationality']
            wallet = register_form.cleaned_data['Wallet']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'polls/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(Name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'polls/register.html', locals())
                same_email_user = models.User.objects.filter(Email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.Name = username
                new_user.Nationality = nationality
                new_user.Email = email
                new_user.password = password1
                new_user.Wallet = wallet
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'polls/register.html', locals())
