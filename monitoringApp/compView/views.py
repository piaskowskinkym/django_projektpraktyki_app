from django.shortcuts import render
from .models import ClassRoom,Computer
from .forms import ComputerForm
from django.http import HttpResponseRedirect
# Create your views here.


def s101(response):
    return render(response, "compView/sala101.html", {})  

def s109(response):
    return render(response, "compView/sala109.html", {})  
    
def s212(response):
    return render(response, "compView/sala212.html", {})
    
def dodaj(response):
   
    cr = ClassRoom.objects.all()        
    if response.POST.get("addComputer"):
        classroom = response.POST.get("select")
        numer = response.POST.get("numer")
        mbrd = response.POST.get("mbrd")
        cpu = response.POST.get("cpu")
        ram = response.POST.get("ram")
        cdrom = response.POST.get("cdrom")
        disc = response.POST.get("disc")
        gpu = response.POST.get("gpu")
        sbrd = response.POST.get("sbrd")
        psu = response.POST.get("psu")
        ncu = response.POST.get("ncu")
        ison = response.POST.get("ison")
        if cdrom == 'clicked':
            cdrom = True
        else:
            cdrom = False
        if ison == 'clicked':
            ison = True
        else:
            ison = False
       
        computer = ClassRoom.objects.get(room = classroom)
        computer.computer_set.create(       classR = classroom, 
                                            num = numer,
                                            mbrd = mbrd,
                                            cpu = cpu,
                                            ram = ram ,
                                            cdr = cdrom,
                                            drive = disc,
                                            gpu = gpu,
                                            sbrd = sbrd,
                                            psu = psu,
                                            ncu = ncu ,
                                            isOn = ison 
                                            )

  
    return render(response, "compView/dodaj.html", {"cr":cr})  
