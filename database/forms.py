from django import forms
from .models import User
import re

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fullName', 'cpf', 'email', 'password', 'dateBirth']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        # Remove qualquer caractere que não seja um número
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11:
            raise forms.ValidationError('O CPF deve ter 11 dígitos.')
        return cpf
