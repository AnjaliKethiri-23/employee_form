from django.shortcuts import render,redirect

# Create your views here.
from app1.form import new_employee
def add_employee(request):
    form=new_employee()
    if request.method == "POST":
        form=new_employee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request,'app1template/home.html',{'form':form})
