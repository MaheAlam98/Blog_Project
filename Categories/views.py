from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_categories(request):
    if request.method=='POST':
        fm=forms.category(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect(add_categories)
    
    else:
         fm=forms.category(request.POST)
         return render(request,'add_category.html',{'category':fm})
        
    