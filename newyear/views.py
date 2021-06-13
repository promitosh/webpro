import datetime
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# to create views write a function that takes a request and return an HttpResponse
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })

# urlpatterns a definite variable
# list of the all allowable urls that can be accessed for
# first argument of path() function is empty string, mean no additional argument

# index is a function name which used in views ,to render request of someone
# views is my file name
