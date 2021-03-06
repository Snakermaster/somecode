"""
表单(用于进行表单数据验证)
"""
from django import forms

from common.models import User
from common.utils import to_md5_hex


class RegisterForm(forms.ModelForm):

    repassword = forms.CharField(max_length=20)
    code = forms.CharField(min_length=6, max_length=6)

    def clean_password(self):
        password = self.cleaned_data['password']
        self.cleaned_data['password'] = to_md5_hex(password)
        return self.cleaned_data['password']

    def clean_repassword(self):
        password = self.cleaned_data['password']
        repassword = to_md5_hex(self.cleaned_data['repassword'])
        if password != repassword:
            raise forms.ValidationError('密码和确认密码不一致')
        return repassword

    class Meta:
        model = User
        fields = ('username', 'password', 'realname', 'tel', 'email')
