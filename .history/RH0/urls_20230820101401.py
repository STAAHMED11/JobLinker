
from django.urls import path
from RH0 import views

urlpatterns=[
    path('',views.index,name='RH0'),
    path('about',views.about,name='about'),
    path('upload-pdf/', upload_pdf, name='upload_pdf'),

]