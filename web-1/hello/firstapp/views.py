# from django.shortcuts import render 
# from django.http import HttpResponse

# Create your views here. 

# def index(request): 
#     return HttpResponse("<h2>Глaвнaя</h2>") 

# def about(request): 
#     return HttpResponse("<h2>0 сайте</h2>") 

# def contact(request): 
#     return HttpResponse("<h2>Koнтaкты</h2>") 

# def products(request, productid): 
#     category = request.GET.get("cat", "11") 
#     output = "<h2>Продукт № {0}  Категория: {1}</h2>" .format(productid, category) 
#     return HttpResponse(output) 

# def users(request): 
#     id = request.GET.get("id", 1) 
#     name = request.GET.get("name", "Максим") 
#     output = "<h2>Пользователь</h2><h3>id: {0}  Имя: {1}</h3 >" .format(id, name) 
#     return HttpResponse(output) 

from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect 

def index(request): 
    return HttpResponse("Index") 
def about(request): 
    return HttpResponse("About") 
def contact(request): 
    return HttpResponseRedirect("/about") 
def details(request): 
    return HttpResponsePermanentRedirect("/") 

#from django.http import * 

# def m304(request): 
#   return HttpResponseNotModified() 
# def m400(request): 
#   return HttpResponseBadRequest("<h2>Bad Request</h2>") 
# def m403(request): 
#   return HttpResponseForЬidden ( "<h2>ForЬidden</h2>") 
# def m404(request): 
#   return HttpResponseNotFound("<h2>Not Found</h2>") 
# def m405(request): 
#   return HttpResponseNotAllowed("<h2>Method is not allowed</h2>") 
# def m410(request): 
#   return HttpResponseGone("<h2>Content is no longer here</h2>") 
