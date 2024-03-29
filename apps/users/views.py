from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password




from users.forms import LoginForm, RegisterForm,ForgetPwdForm,ModifyForm
from .models import UserProfile,EmailVerifyRecord
from .utils.email_send import send_register_email
# Create your views here.


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if active_code:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email = email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")

        return render(request, "login.html", {})


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email=username),password = password)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST['email']
            if UserProfile.objects.filter(email = user_name):
                return render(request, 'register.html', {'register_form': register_form,"msg": "用户已存在！"})

            pass_word = request.POST['password']
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name, "register")

            return render(request, "login.html", {})
        else:
            return render(request, 'register.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html",{})

    def post(self,request):
        #对用户名和密码做一个验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户名或密码错误！"})

            else:
                return render(request, "login.html", {"msg": "用户未激活！"})

        else:
            return render(request, "login.html", {"login_form":login_form})
         # return redirect('index')


class ForgetPwdView(View):
    def get(self,request):
        forget_form = ForgetPwdForm()
        return render(request, "forgetpwd.html", {'forget_form':forget_form})

    def post(self, request):
        # 对邮箱地址一个验证
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            email = request.POST['email']
            send_register_email(email, "forget")
            return render(request, "send_success.html", {})
        else:
            return render(request, "forgetpwd.html", {'forget_form':forget_form})
        # if email is not None:
            #     if email.is_active:
            #         login(request, email)
            #         return render(request, "index.html")
            #     else:
            #         return render(request, "login.html", {"msg": "用户名或密码错误！"})
            #

class ResetUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if active_code:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html",{"email":email})
        else:
            return render(request, "active_fail.html")

        return render(request, "login.html", {})


class ModifyPwdView(View):
    def post(self,request):
        modify_from = ModifyForm(request.POST)
        if modify_from.is_valid():
            pwd1 = request.POST['password1']
            pwd2 = request.POST['password2']
            email = request.POST['email']
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email":email,"msg":"密码不一致！"})

            user = UserProfile.objects.get(email= email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, "login.html")
        else:
            email = request.POST['email']
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_from})





