from django.urls import path
from .views import *

app_name = 'postt'
urlpatterns = [
   
   path('index/', post_index, name='index'),
   path('kapali/', post_index, name='kapali'),
   path('create/', post_create, name='create'),
   path('detail/<slug:slug>/', post_detail, name='detail'),
   path('update/<slug:slug>', post_update, name='update'),
   path('update/comment/<int:pk>',comment_update, name='com_update'),
   path('delete/<slug:slug>', post_delete, name='delete'),
   path('delete/comment/<int:pk>', comment_delete, name='com_delete'),
   
]

