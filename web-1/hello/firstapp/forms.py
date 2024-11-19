from django import forms

class UserForm(forms.Form):
#    name = forms.CharField()
#    age = forms.IntegerField()
    name = forms.CharField(label='Имя клиента')
    age = forms.IntegerField(label='Возраст клиента')
