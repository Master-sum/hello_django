from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .forms import signup_form,login_form
from .models import User
from django.http import HttpResponse
#登录视图
class user_login_view(View):
    def get(self,request):
        return render(request,'user/login.html')
    def post(self,request):
        form = login_form(request.POST)
        if form.is_valid():

            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('blog:index'))
            else:
                print("用户名或者密码错误！")
                return redirect(reverse('user:login'))
        else:
            error = form.errors.get_json_data
            print(error)
            return redirect(reverse('user:login'))

#注册视图
class user_singup_view(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self,request):
        forms = signup_form(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            user.password = forms.cleaned_data.get('registerPassword')
            print(user)
            user.save()
            return redirect(reverse('blog:index'))
        else:
            error = forms.errors.get_json_data()
            print(error)
            return redirect(reverse('user:signup'))


