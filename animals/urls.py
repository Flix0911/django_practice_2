"""
URL configuration for animals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# import our view from pets
from pets.views import TurtleView, TurtleViewID
# import views from dogs
from dogs.views import Dog_View, Dog_View_ID
from cats.views import Cat_View, Cat_View_ID
# import from birds
from birds.views import Bird_View, Bird_View_ID

urlpatterns = [
    path('admin/', admin.site.urls),
    # add new url pattern ~ this will handle all requests to URL
    path("turtle/", TurtleView.as_view()),
    path('turtle/<id>/', TurtleViewID.as_view()),
    path('dog/', Dog_View.as_view()),
    path('dog/<id>/', Dog_View_ID.as_view()),
    path('cat/', Cat_View.as_view()),
    path('cat/<id>/', Cat_View_ID.as_view()),
    path('bird/', Bird_View.as_view()),
    path('bird/<id>/', Bird_View_ID.as_view())
]


# /turtle/ get & create route
# /turtle/:id show, update, and delete route
