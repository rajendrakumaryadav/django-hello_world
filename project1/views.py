from django.shortcuts import render


# Create your views here.
def hello_view(request):
    return render(request, "project1.html")
