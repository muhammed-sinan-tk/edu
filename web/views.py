
from django.shortcuts import render
from . models import Product,Contact,School,About
def index(request):
    context={
        'produ':Product.objects.all(),
    }
    return render(request,'web/index.html',context)

def school(request):
    context={
        'school':School.objects.all(),
    }
    return render(request,'web/team.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST.get("Full_Name")
        email=request.POST.get("email")
        Message=request.POST.get("Subject")
        Subject=request.POST.get("Message")
        
        contact1=Contact(
            Full_Name=name,
            email=email,
            Subject=Subject,
            Message=Message,
        )
        contact1.save() 
    return render (request,'web/contact.html')

def about(request):
    context={
        'teacher':About.objects.all(),
    }
    return render (request,'web/about.html',context)

def photo(request):
   
    return render (request,'web/gallery.html')

def class1(request):
   
    return render (request,'web/class.html')
