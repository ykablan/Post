from django.urls import path
from .views import index, create,detail,update,delete

app_name = 'customer'
urlpatterns = [
   path('index/', index, name='index'),
   path('create/', create, name='create'),
   path('detail/<int:pk>/', detail, name='detail'),
   path('update/<int:pk>', update, name='update'),
   path('delete/<int:pk>', delete, name='delete'),
]

