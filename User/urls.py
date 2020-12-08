from django.urls import path

from . import views

urlpatterns = [
       path("homepage",views.book,name="book"),
       path("login",views.login,name="login"),
       path("form", views.form, name="form"),
       path("logout",views.logout,name="logout"),
       path("doubt",views.doubt,name="doubt"),

]