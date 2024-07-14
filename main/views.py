from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request ,'index.html')

def login_view(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        print(username, password)
    return render(request,'login.html')
def register_view(request):
    if request.method=='POST':
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('pwd')
        cpassword= request.POST.get('cpwd')
        print(username,email,password,cpassword)
    return render(request,'register.html')

