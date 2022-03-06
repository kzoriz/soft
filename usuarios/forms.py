from django.contrib.auth import forms as nforms
from models import User, Funcionario, Discente
from django import forms as mforms
from django import forms


class UserChangeForm(nforms.UserChangeForm):
    class Meta(nforms.UserChangeForm.Meta):
        model = User


class UserCreationForm(nforms.UserCreationForm):
    class Meta(nforms.UserCreationForm.Meta):
        model = User


class FuncionarioForm(mforms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'


class DiscenteForm(forms.ModelForm):
    class Meta:
        model = Discente
        fields = "__all__"

