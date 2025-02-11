from django.urls import path
from .views import post_index, post_create, post_detail, post_update, post_delete

app_name = 'postt'
urlpatterns = [
   path('index/', post_index, name='index'),
   path('create/', post_create, name='create'),
   path('detail/<slug:slug>/', post_detail, name='detail'),
   path('update/<slug:slug>', post_update, name='update'),
   path('delete/<slug:slug>', post_delete, name='delete'),
]

