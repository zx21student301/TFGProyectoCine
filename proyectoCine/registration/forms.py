from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email","username","first_name", "last_name", "password1", "password2")
    
    def clean_email(self):
        correo = self.cleaned_data.get("email")
        
        #comprobar que el email no exite
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError("Error: Ya hay un Usuario con este correo")
        
        return correo