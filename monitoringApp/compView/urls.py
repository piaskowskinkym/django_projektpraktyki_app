from django.urls import path
from . import views

urlpatterns =[
    path("s105/", views.s105, name="s105"),
    path("s109/", views.s109, name="s109"),
    path("s121/", views.s121, name="s121"),
    path("s117/", views.s117, name="s117"),
    path("s2/", views.s2, name="s2"),
    path("s3/", views.s3, name="s3"),
    path("s4/", views.s4, name="s4"),
    path("dodaj/", views.dodaj, name="dodaj")
]