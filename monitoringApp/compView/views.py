from django.shortcuts import render
from .models import ClassRoom,Computer
from .forms import ComputerForm
from django.http import HttpResponseRedirect

# Create your views here.


def s105(response):

    cr = Computer.objects.filter(classR = "3")
    return render(response, "compView/sala105.html", {"cr":cr})  
def home(response):

    return render(response, "compView/home.html", {})  
    
def s117(response):

    cr = Computer.objects.filter(classR = "4")
    return render(response, "compView/sala117.html", {"cr":cr})     

def s109(response):
    cr = Computer.objects.filter(classR = "1")
    return render(response, "compView/sala109.html", {"cr":cr})  
    
def s121(response):
    cr = Computer.objects.filter(classR = "2")
    return render(response, "compView/sala121.html", {"cr":cr})
def s2(response):
    cr = Computer.objects.filter(classR = "5")
    return render(response, "compView/sala2.html", {"cr":cr})
    
def s3(response):
    cr = Computer.objects.filter(classR = "6")
    return render(response, "compView/sala3.html", {"cr":cr})
    
def s4(response):
    cr = Computer.objects.filter(classR = "7")
    return render(response, "compView/sala4.html", {"cr":cr})
    
    
def dodaj(response):
    if response.method == "POST":
        form = ComputerForm(response.POST)
        if form.is_valid():
            croom = form.cleaned_data["croom"]
            name = form.cleaned_data["name"]
            ip = form.cleaned_data["ip"]
            sys = form.cleaned_data["sys"]
            cpu = form.cleaned_data["cpu"]
            ison = form.cleaned_data["ison"]

            computer = ClassRoom.objects.get(room = croom)

            computer.computer_set.create(   
                                            classR = croom, 
                                            name = name,
                                            cpu = cpu,
                                            sys = sys,
                                            ip = ip,
                                            isOn = ison
                                            )

    else:
        form = ComputerForm()
    return render(response, "compView/dodaj.html", {"form":form})  
