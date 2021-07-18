from django.shortcuts import redirect, render
from django.http import HttpResponse
from requests.api import delete, get
from .forms import IpForm
from .api import getinfo
# Create your views here.
def home(request):
    context = {

    }
    return render(request,"base.html",context)

def base(request):
    x = ""
    if request.method=="POST":
        form = IpForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['ip']
            x += str(ip)
        else:
            return redirect("/results/")
    result = getinfo(x)
    print(result)
    return render(request,"results.html",result)

def output(request):
    return render(request,"output.html")