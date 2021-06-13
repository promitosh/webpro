from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

]
# urlpatterns a definite variable list of the all allowable urls that can be accessed for
# first argument of path() function is empty string, mean no additional argument
# index is a function name which used in views file to render request of someone
# views is  file name
