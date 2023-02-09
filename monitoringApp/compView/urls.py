from django.urls import path
from . import views

urlpatterns =[
    path("s101/", views.s101, name="s101"),
    path("s109/", views.s109, name="s109"),
    path("s212/", views.s212, name="s212"),
    path("dodaj/", views.dodaj, name="dodaj"),
]