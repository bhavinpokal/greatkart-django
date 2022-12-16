from crispy_forms.helper import FormHelper
from django import forms

from .models import Account, UserProfile


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '(xxx)xxx-xxxx'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __int__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        helper = FormHelper()

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match!'
            )


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    phone_number = forms.CharField(label='Phone Number')
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number']

    def __int__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        helper = FormHelper()


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False,
        error_messages={'invalid': 'Image files only', },
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Profile Picture',
    )

    address_line_1 = forms.CharField(label='Address Line 1')
    address_line_2 = forms.CharField(label='Address Line 2')

    class Meta:
        model = UserProfile
        fields = ['address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture']

    def __int__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        helper = FormHelper()
