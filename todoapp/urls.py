from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecompleted', views.deleteCompletedTodo, name='deletecompleted'),
    path('deleteall', views.deleteAllTodo, name='deleteall'),
]