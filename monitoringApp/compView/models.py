from django.db import models


# Create your models here.
class ClassRoom(models.Model):
    room = models.CharField(max_length=200, default ="sala")
    def __str__(self):
        return self.room

class Computer(models.Model):
    classR = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default ="test")
    ip = models.CharField(max_length=200, default ="test")
    sys = models.CharField(max_length=200, default ="test")
    cpu = models.CharField(max_length=200, default ="test")
    isOn = models.BooleanField()
    
    def __str__(self):
        return self.name