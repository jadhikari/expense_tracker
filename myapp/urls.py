from django.urls import path
from . import views  # Make sure views.py is in the same directory as urls.py


app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]