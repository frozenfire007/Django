from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def root_page(request):
    return render(request, template_name="myapp/root_page.html")

def temp_inherit_home(request):
    return render(request, template_name="myapp/inherit_page.html")
def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")

def classroom(request):
    classrooms = [
        {"name": "one", "address": "BKT"},
        {"name": "Two", "address": "KTM"},
        {"name": "Three", "address": "LTP"},
        {"name": "Four", "address": "PKR"}
        ]
    return render(request, template_name="myapp/classroom.html", context={"classroom_name": "One","location":"KTM", "classrooms": classrooms})
    
