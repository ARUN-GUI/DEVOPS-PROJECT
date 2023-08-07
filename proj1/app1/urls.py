from . import views
from django.urls import path

urlpatterns = [path('',views.index,name='index'),
               path('add/',views.add,name='add'),
               path('add/addrecord/',views.addrecord,name='addrecord'),
               path('delete/<int:id>',views.delete,name='delete'),]