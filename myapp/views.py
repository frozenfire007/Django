from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def root_page(request):
    return render(request, template_name="myapp/root_page.html")

def temp_inherit_home(request):
    return render(request, template_name="myapp/inherit_page.html")
    
