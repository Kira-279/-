from django.shortcuts import render 
from django.http import *
from django.template.response import TemplateResponse 
from .forms import UserForm
from django.http import HttpResponseRedirect 
from .models import Person 

def index(request):
    people = Person.objects.all() 
    return render(request, "index.html", {"people": people}) 

def create(request): 
    if request.method == "POST": 
        klient = Person() 
        klient.name = request.POST.get("name") 
        klient.age = request.POST.get("age") 
        klient.save() 
    return HttpResponseRedirect("/") 

# изменение данных в БД 
def edit(request, id): 
    try: 
        person = Person.objects.get(id=id) 
        if request.method == "POST": 
            person.name = request.POST.get("name") 
            person.age = request.POST.get("age") 
            person.save() 
            return HttpResponseRedirect("/") 
        else: 
            return render(request, "edit.html", {"person": person}) 
    except Person.DoesNotExist: 
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")
    
def delete(request, id): 
    try: 
        person = Person.objects.get(id=id) 
        person.delete() 
        return HttpResponseRedirect("/") 
    except Person.DoesNotExist: 
        return HttpResponseNotFound("<h2>Клиент не найден</h2>") 

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

#    if request.method == "POST":
#        name = request.POST.get("name") # получить значения поля Имя
#        age = request.POST.get("age") # значения поля Возраст
#        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст – {1}</h3>".format(name, age)
#        return HttpResponse(output)
#    else:
#    userform = UserForm() 
#   if request.method == "POST": 
#        userform = UserForm(request.POST)
#        if userform.is_valid(): 
#            name = userform.cleaned_data["name"] 
#            age = userform.cleaned_data["age"]
#            return HttpResponse("<h2>Имя введено коррректно – {0} {1}</h2>".format(name, age)) 
#    return render(request, "firstapp/index.html", {"form": userform}) 
#  
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




