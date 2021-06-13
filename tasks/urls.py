from django.urls import path

from . import views


app_name = "tasks"
# app_name is used to fix up name collision
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    # index is a function name which used in views ,to render request of someone
    # views is my file name


]
