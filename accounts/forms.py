from django import forms
from django.contrib.auth import get_user_model

from utils.messages import SYSTEM_ERR_MSG

User = get_user_model()


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        min_length=6,
        required=False)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        min_length=6,
        required=False)

    class Meta:
        model = User
        fields = (
            'name',
            'mobile_number',
            'email',
        )

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        error_dict = {}

        if cleaned_data.get('password1') or cleaned_data.get('password2'):
            if not (cleaned_data.get('password1') == cleaned_data.get('password2')):
                error_dict['password2'] = "Passwords don't match"
        if error_dict:
            raise forms.ValidationError(error_dict)
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """
    User login form
    """

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        required=True
    )

    def clean(self):
        if not self.cleaned_data.get('email'):
            raise forms.ValidationError({"email": SYSTEM_ERR_MSG['EMAIL_REQUIRED']})
        if not self.cleaned_data.get('password'):
            raise forms.ValidationError({"password": SYSTEM_ERR_MSG['PASSWORD_REQUIRED']})
        return self.cleaned_data
