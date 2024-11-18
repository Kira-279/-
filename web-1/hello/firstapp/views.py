from django.shortcuts import render 
from django.http import *
from django.template.response import TemplateResponse 

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


def index(request): 
#    header = "Персональные данные"  # обычная переменная 
#    langs = ["Английский", "Немецкий", "Испанский"]  # массив 
#    user = {"name": "Максим,", "age": 30}  # словарь 
#    addr = ("Виноградная", 23, 45)  # кортеж 
#    data = {"header": header, "langs": langs, "user": user, "address": addr} 
#    return render(request, "firstapp/index_app1.html", context=data)
#    return render(request, "firstapp/home.html")
    return render(request, "firstapp/index.html")


