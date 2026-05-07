from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User


class RegistroUsuarioForm(UserCreationForm):
    ROL_CHOICES = (
        ('Estudiante', 'Estudiante'),
        ('Docente', 'Docente'),
    )

    email = forms.EmailField(label='Correo electronico', required=True)
    rol = forms.ChoiceField(label='Rol', choices=ROL_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Usuario',
        }

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Ya existe un usuario con ese correo.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            grupo, _ = Group.objects.get_or_create(name=self.cleaned_data['rol'])
            user.groups.add(grupo)

        return user
