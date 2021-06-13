from django.urls import path

from . import views
# several routes
# urlpatterns a definite variable list of the all allowable urls that can be accessed for
# first argument of path() function is empty string, mean no additional argument
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.greet, name='greet'),
    path('promit', views.promit, name='promit'),
    path('akor', views.akor, name='akor'),
]
# routes
