from django.shortcuts import render
# Create your views here.
def homeview(request):
    return render(request,'testapp/Home.html')

def pythonsyllabus(request):
    return render(request,'testapp/python.html')

def corejavasyllabus(request):
    return render(request,'testapp/CoreJava.html')

def advjavasyllabus(request):
    return render(request,'testapp/advjava.html')

def cplusplussyllabus(request):
    return render(request,'testapp/C++.html')

def csyllabus(request):
    return render(request,'testapp/csyllabus.html')

def register(request):
    return render(request,'testapp/register.html')

def faq(request):
    return render(request,'testapp/faq.html')

def contactus(request):
    return render(request,'testapp/contactus.html')

def about(request):
    return render(request,'testapp/about.html')

def join(request):
    return render(request,'testapp/join.html')

def social(request):
    return render(request,'testapp/social.html')

def fb(request):
    return render(request,'testapp/fb.html')
