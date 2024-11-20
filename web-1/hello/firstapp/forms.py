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
#    file = forms.FileField(label="Файл")
#    file = forms.ImageField(label="Изображение") 
#    date = forms.DateField(label="Введите дату")
#    time = forms.DateField(label="Введите время")
#    date_time = forms.DateTimeField(label="Введите дату и время") 
#    time_delta = forms.DurationField(label="Введите промежуток времени")
#    date_time = forms.SplitDateTimeField(label="Введите дату и время") 
#    num = forms.IntegerField(label="Введите целое число")
#    num1 = forms.DecimalField(label="Введите десятичное число", decimal_places=2)
#    num2 = forms.FloatField(label="Введите число") 
#    ling = forms.ChoiceField(label="Выберите язык", choices=((1, "Английский"), (2, "Немецкий"), (3, "Французский"))) 
#    city = forms.TypedChoiceField(label="Выберите город", empty_value=None, choices=((1, "Москва"), (2, "Воронеж"), (3, "Курск")))
#    country = forms.MultipleChoiceField(label="Выберите страны", choices=((1, "Англия"), (2, "Германия"), (3, "Испания"), (4, "Россия"))) 
    name = forms.CharField(label="Имя", min_length=3, widget=forms.TextInput(attrs={"class": "myfield"})) 
    age = forms.IntegerField(label="Возраст", min_value=1, max_value=100, widget=forms.NumberInput(attrs={"class": "myfield"})) 
#    required_css_class = "field" 
#    error_css_class = "error" 
#    email = forms.EmailField(label="Электронный адрес") 
#    reklama = forms.BooleanField(label="Согласны получать рекламу", required=False) 
#    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
#    field_order = ["age", "name"] 
    




