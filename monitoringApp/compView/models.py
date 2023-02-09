from django.db import models

# Create your models here.
class ClassRoom(models.Model):
    room = models.CharField(max_length=200, default ="sala")
    def __str__(self):
        return self.room

class Computer(models.Model):
    classR = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    num = models.CharField(max_length=200, default ="test")
    mbrd = models.CharField(max_length=200, default ="test")
    cpu = models.CharField(max_length=200, default ="test")
    ram = models.CharField(max_length=200, default ="test")
    cdr = models.BooleanField()
    drive = models.CharField(max_length=200, default ="test")
    gpu = models.CharField(max_length=200, default ="test")
    sbrd = models.CharField(max_length=200, default ="test")
    psu = models.CharField(max_length=200, default ="test")
    ncu = models.CharField(max_length=200, default ="test")
    isOn = models.BooleanField()
    def __str__(self):
        return self.num    