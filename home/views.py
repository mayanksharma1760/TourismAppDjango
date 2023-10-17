from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("this is a Homepage")
    return render(request,"index.html")

def about(request):
    # return HttpResponse("this is about pag")
    return render(request,"about.html")

def service(request):
    return HttpResponse("this is services oage ")


def contact(request):
    return render(request,"contact.html")