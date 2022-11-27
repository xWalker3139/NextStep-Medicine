from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor, Pacient, Reteta, Adauga_Cabinet, Adauga_Pacienti, Servicii, Recenzii, Programare

class DoctorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele tau...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Parola...'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Verifica-ti parola...'}),
        }

class PacientForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele tau...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Parola...'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Verifica-ti parola...'}),
        }

class DoctorNewForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user1', 'type':'hidden'}),
            'numele':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele tau...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
            'nr_de_telefon':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numar de telefon...'}),
            'imagine':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Adauga o imagine...'})
        }

class PacientNewform(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user1', 'type':'hidden'}),
            'numele':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele tau...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
            'nr_de_telefon':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numar de telefon...'}),
            'imagine':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Adauga o imagine...'})
        }

class RetetaForm(forms.ModelForm):
    class Meta:
        model = Reteta
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user1', 'type':'hidden'}),
            'nume':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele retetei...'}),
            'imagine':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Adauga reteta...'}),
        }

class AdaugaCabinetForm(forms.ModelForm):
    class Meta:
        model = Adauga_Cabinet
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user1', 'type':'hidden'}),
            'numele_cabinetului':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele cabinetului...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
            'nr_de_telefon':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numar de telefon...'}),
            'categorie':forms.Select(attrs={'class':'form-control', 'placeholder':'Categorie...'}),
            'judet':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Judet...'}),
            'localitate':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Localitate...'}),
            'CUI':forms.TextInput(attrs={'class':'form-control', 'placeholder':'CUI...'}),
            'date_firma':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date firma...'}),
            'registrul_comertului':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Registrul comertului...'}),
            'descriere':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descriere...'}),
            'specializare':forms.Select(attrs={'class':'form-control', 'placeholder':'Specializare...'}),
            'imagine':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Introdu o imagine...'}),
            'imagine2':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Introdu o imagine...'}),
            'imagine3':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Introdu o imagine...'}),
            'imagine4':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Introdu o imagine...'}),
            'imagine5':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Introdu o imagine...'}),
            'imagine6':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Introdu o imagine...'}),
            'de_la1':forms.Select(attrs={'class':'form-control', 'placeholder':'De la...', 'autocomplete':'off'}),
            'pana_la1':forms.Select(attrs={'class':'form-control', 'placeholder':'Pana la...', 'autocomplete':'off'}),
            'de_la2':forms.Select(attrs={'class':'form-control', 'placeholder':'De la...', 'autocomplete':'off'}),
            'pana_la2':forms.Select(attrs={'class':'form-control', 'placeholder':'Pana la...', 'autocomplete':'off'}),
            'de_la3':forms.Select(attrs={'class':'form-control', 'placeholder':'De la...', 'autocomplete':'off'}),
            'pana_la3':forms.Select(attrs={'class':'form-control', 'placeholder':'Pana la...', 'autocomplete':'off'}),
            'de_la4':forms.Select(attrs={'class':'form-control', 'placeholder':'De la...', 'autocomplete':'off'}),
            'pana_la4':forms.Select(attrs={'class':'form-control', 'placeholder':'Pana la...', 'autocomplete':'off'}),
            'de_la5':forms.Select(attrs={'class':'form-control', 'placeholder':'De la...', 'autocomplete':'off'}),
            'pana_la5':forms.Select(attrs={'class':'form-control', 'placeholder':'Pana la...', 'autocomplete':'off'}),
            'de_la6':forms.Select(attrs={'class':'form-control', 'placeholder':'De la...', 'autocomplete':'off'}),
            'pana_la6':forms.Select(attrs={'class':'form-control', 'placeholder':'Pana la...', 'autocomplete':'off'}),
            'de_la7':forms.Select(attrs={'class':'form-control', 'placeholder':'De la...', 'autocomplete':'off'}),
            'pana_la7':forms.Select(attrs={'class':'form-control', 'placeholder':'Pana la...', 'autocomplete':'off'}),
        }

class Adauga_PacientiForm(forms.ModelForm):
    class Meta:
        model = Adauga_Pacienti
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user1', 'type':'hidden'}),
            'numele':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele...'}),
            'prenumele':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prenumele...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
            'nr_de_telefon':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numar de telefon...'}),
            'data_nasterii':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Data nasterii...'}),
            'sex':forms.Select(attrs={'class':'form-control', 'placeholder':'Sex...'}),
            'judet':forms.Select(attrs={'class':'form-control', 'placeholder':'Judet...'}),
            'localitate':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Localitate...'}),
            'adresa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresa...'}),
        }

class ServiciiForm(forms.ModelForm):
    class Meta:
        model = Servicii
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'value':'', 'id':'user1', 'type':'hidden'}),
            'cabinet':forms.TextInput(attrs={'value':'', 'id':'cabinet', 'type':'hidden'}),
            'categorie':forms.Select(attrs={'class':'form-control', 'placeholder':'Categorie...'}),
            'servicii':forms.Select(attrs={'class':'form-control', 'placeholder':'Servicii...'}),
            'pret':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pret...'}),
            'moneda':forms.Select(attrs={'class':'form-control', 'placeholder':'Moneda...'}),
        }

class RecenziiForm(forms.ModelForm):
    class Meta:
        model = Recenzii
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'name':'user', 'type':'hidden'}),
            'cabinet':forms.TextInput(attrs={'class':'form-control', 'id':'produs1', 'value':'', 'name':'produs', 'type':'hidden'}),
            'descriere':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Mesajul tau...'}),
        }

class ProgramareForm(forms.ModelForm):
    class Meta:
        model = Programare
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'name':'user'}),
            'afacere':forms.TextInput(attrs={'class':'form-control', 'id':'produs1', 'value':'', 'name':'produs'}),
            'data':forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Data...'}),
            'ora':forms.Select(attrs={'class':'form-control', 'placeholder':'La ce ora vrei sa iti faci programare...'}),
        }