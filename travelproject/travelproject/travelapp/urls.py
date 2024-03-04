from . import views
from django.urls import path

urlpatterns = [
    path('',views.part,name='part')
    path('add/',views.addition,name='addition')
    path('substract/',views.substraction,name='substraction')
    path('multiplication/',views.multiplication,name='multiplication')
    path('division/',views.division,name='division')

6
]



