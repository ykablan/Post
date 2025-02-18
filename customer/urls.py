from django.urls import path
from .views import index, create,detail,update,delete,contact_update, contact_delete

app_name = 'customer'
urlpatterns = [
   path('index/', index, name='index'),
   path('create/', create, name='create'),
   path('detail/<int:pk>/', detail, name='detail'),
   path('update/<int:pk>', update, name='update'),
   path('update/contact/<int:pk>',contact_update, name='con_update'),
   path('delete/<int:pk>', delete, name='delete'),
   path('delete/contact/<int:pk>', contact_delete, name='con_delete'),
]

