from django import forms

class UserForm(forms.Form):
#    name = forms.CharField()
#    age = forms.IntegerField()
#    name = forms.CharField(label='Имя клиента')
#    age = forms.IntegerField(label='Возраст клиента')

#    basket = forms.BooleanField(label="Положить товар в корзину", required=False)
#  
#    vyb = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")
#    name = forms.CharField(label="Имя клиента", required=False, max_length=15, help_text="ФИO не более 15 символов")
#    email = forms.EmailField(label="Электронный адрес", help_text="Обязательный символ - @")
#    ip_adres = forms.GenericIPAddressField(label="IP адрес", help_text=" Пример формата 192.0.2.0") 
#    reg_text = forms.RegexField(label="Текст", regex="^[0-9][A-F][0-9]$")
#    slug_text = forms.SlugField(label="Введите текст")
#    url_text = forms.URLField(label="Введите URL", help_text="Например http://www.google.com")
#    uuid_text = forms.UUIDField(label="Введите UUID", help_text="Формат xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx") 
#       combo_text = forms.ComboField(label="Введите URL", fields=[forms.URLField(), forms.CharField(max_length=20)])
#    file_path = forms.FilePathField(label="Выберите файл", path="C:", allow_files="True", allow_folders="True")
    file = forms.FileField(label="Файл")