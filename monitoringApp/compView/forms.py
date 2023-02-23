from django import forms

SALE_CHOICES=(
    ("sala2", "Sala 2"),
    ("sala3", "Sala 3"),
    ("sala4", "Sala 4"),
    ("sala105", "Sala 105"),
    ("sala109", "Sala 109"),
    ("sala117", "Sala 117"),
    ("sala121", "Sala 121"),
)
#Create
class ComputerForm(forms.Form):
    croom = forms.ChoiceField(label="Wybierz Salę",choices=SALE_CHOICES)
    name = forms.CharField(label="Nazwa", max_length=200)
    ip = forms.CharField(label="Ip", max_length=200)
    sys = forms.CharField(label="System", max_length=200)
    cpu = forms.CharField(label="Procesor" ,max_length=200)
    ison = forms.BooleanField(label="Włączony?", required=False)