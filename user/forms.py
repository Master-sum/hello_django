from django import forms
from .models import User
#注册表单
class signup_form(forms.ModelForm):
    registerPasswords = forms.CharField(max_length=10,min_length=6)
    registerPassword = forms.CharField(max_length=10,min_length=6)
    def clean(self):
        cleaned_data = super(signup_form, self).clean()
        print(cleaned_data)
        password = cleaned_data.get('registerPassword')
        password1 = cleaned_data.get('registerPasswords')
        print(password,password1)
        if password != password1:
            raise forms.ValidationError(message="两次密码不一致")
        print(cleaned_data)
        return cleaned_data
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exis = User.objects.filter(telephone=telephone).exists()
        if exis:
            raise forms.ValidationError(message='%s手机号码被注册'%telephone)
        return telephone
    class Meta:
        model = User
        exclude = ['password']
        # fields = '__all__'
#登录表单
class login_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']#提取登录的属性字段