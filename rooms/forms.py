from django.forms import ModelForm
from .models import Contact
from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name','surname','subject','email')




class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username =self.cleaned_data_get('username')
        password = self.cleaned_data_get('password')

        if username and password:
            user = authenticate(username=username , password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active():
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm,self.clean(*args,**kwargs))    






class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']            