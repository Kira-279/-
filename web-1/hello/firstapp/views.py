from django.shortcuts import render 
from django.http import *
from django.template.response import TemplateResponse 
from .forms import UserForm
from django.shortcuts import render 

# def index(request): 
#    return TemplateResponse(request, "firstapp/home.html")

# def index(request): 
#     return render(request, "index.html") 

# def index(request): 
#    return render(request, "firstapp/home.html") 

# def index(request):  
#     data = {"header": "Передача параметров в шаблон Django", 
#             "message": "Загружен шаблон templates/firstapp/index_app1.html"} 
#   return render(request, "firstapp/index_app1.html", context=data) 

# def index(request): 
# header = "Персональные данные"  # обычная переменная 
# langs = ["Английский", "Немецкий", "Испанский"]  # массив 
# user = {"name": "Максим,", "age": 30}  # словарь 
# addr = ("Виноградная", 23, 45)  # кортеж 
# data = {"header": header, "langs": langs, "user": user, "address": addr} 
# return TemplateResponse(request, "index.html", data) 


# def index(request): 
#    header = "Персональные данные"  # обычная переменная 
#    langs = ["Английский", "Немецкий", "Испанский"]  # массив 
#    user = {"name": "Максим,", "age": 30}  # словарь 
#    addr = ("Виноградная", 23, 45)  # кортеж 
#    data = {"header": header, "langs": langs, "user": user, "address": addr} 
#    return render(request, "firstapp/index_app1.html", context=data)
#    return render(request, "firstapp/home.html")
#    data = {"age": 66}
#   cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
#    cat = []
#    userform = UserForm()
#    return render(request, "firsatapp/index.html", {"form": userform})

def index(request):
#    if request.method == "POST":
#        name = request.POST.get("name") # получить значения поля Имя
#        age = request.POST.get("age") # значения поля Возраст
#        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст – {1}</h3>".format(name, age)
#        return HttpResponse(output)
#    else:
    userform = UserForm() 
    if request.method == "POST": 
        userform = UserForm(request.POST)
        if userform.is_valid(): 
            name = userform.cleaned_data["name"] 
            age = userform.cleaned_data["age"]
            return HttpResponse("<h2>Имя введено коррректно – {0} {1}</h2>".format(name, age)) 
    return render(request, "firstapp/index.html", {"form": userform})  
#        if userform.is_valid(): 
#           name = userform.cleaned_data["name"] 
#            return HttpResponse("<h2>Имя введено коррректно – {0}</h2>".format(name)) 
#        else: 
#            return HttpResponse("Ошибка ввода данных") 
#    else: 
#        userform = UserForm() 
#        return render(request, "firstapp/index.html", {"form": userform})

#def products(request, productid = 1):
#     output = "<h2>Продукт № {0}</h2>".format(productid)
#     return HttpResponse(output)

#def users(request, id=1, name= 'Максим'):
#    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1} </h3>".format(id,name)
#    return HttpResponse(output)




