from django.shortcuts import render

# Create your views here.
def common_home(request):
    return render(request,'commontemp/index.html')

def common_todo(request):
    return render(request,'commontemp/todo.html')  

def common_new(request):
    return render(request,'commontemp/new.html')
    
def common_anim(request):
    return render(request,'commontemp/animation.html')
def common_new1(request):
    return render(request,'commontemp/new2.html')  

def common_new10(request):
    return render(request,'commontemp/database.html')           